use sha2::{Digest,Sha256};use std::{env,fs,process};const MAGIC:&[u8]=b"AUR0";const VERSION:u8=0x01;const XOR_MASK:u8=0x42;
const CKSUM_MULT:u64=0x5f3759df;const SALT:&[u8]=b"aurora_ctf_2025_secret_salt";const OFF_MAGIC:usize=0;const OFF_VER:usize=4;
const OFF_ULEN:usize=5;const OFF_DATA:usize=6;const SZ_MAGIC:usize=4;const SZ_VER:usize=1;const SZ_ULEN:usize=1;const SZ_EXPIRY:usize=8;
const SZ_FLAGS:usize=2;const SZ_HASH:usize=32;const MIN_LIC_SIZE:usize=SZ_MAGIC+SZ_VER+SZ_ULEN+SZ_EXPIRY+SZ_FLAGS+SZ_HASH;
const FLAG_PREMIUM:u16=1<<0;const FLAG_ENTERPRISE:u16=1<<1;const FLAG_DEBUG:u16=1<<2;const FLAG_TRIAL:u16=1<<3;
const FLAG_MASK:u16=FLAG_PREMIUM|FLAG_ENTERPRISE|FLAG_DEBUG|FLAG_TRIAL;const FLAG_INVALID_COMBO:u16=FLAG_TRIAL|FLAG_ENTERPRISE;
type Timestamp=i64;type FeatureSet=u16;type HashDigest=[u8;32];type Result<T>=std::result::Result<T,&'static str>;
struct LicenseInfo{username:String,expiry:Timestamp,flags:FeatureSet,hash:String,}
#[inline(always)]const fn has_flag(f:FeatureSet,b:FeatureSet)->bool{(f&b)!=0}
#[inline(always)]const fn validate_flags(f:FeatureSet)->bool{(f&!FLAG_MASK)==0&&(f&FLAG_INVALID_COMBO)!=FLAG_INVALID_COMBO}
#[inline(always)]fn xor_bytes(b:&[u8],k:u8)->Vec<u8>{b.iter().map(|&x|x^k).collect()}
macro_rules!die{($($arg:tt)*)=>{{eprintln!($($arg)*);process::exit(1);}};}
macro_rules!chk{($pos:expr,$sz:expr,$max:expr,$err:expr)=>{if($pos+$sz)>$max{return Err($err);}};}
macro_rules!rd_u16{($d:expr,$p:expr)=>{u16::from_be_bytes(unsafe{*($d.as_ptr().add($p)as*const[u8;2])})};} 
macro_rules!rd_i64{($d:expr,$p:expr)=>{i64::from_be_bytes(unsafe{*($d.as_ptr().add($p)as*const[u8;8])})};} 
macro_rules!rd_u8{($d:expr,$p:expr)=>{unsafe{*$d.get_unchecked($p)}};}
macro_rules!rd_slice{($d:expr,$p:expr,$sz:expr)=>{unsafe{$d.get_unchecked($p..$p+$sz)}};}
fn parse_license(data:&[u8])->Result<LicenseInfo>{let(dlen,mut pos)=(data.len(),OFF_MAGIC);if dlen<MIN_LIC_SIZE{return Err("truncated license");}
if rd_slice!(data,pos,SZ_MAGIC)!=MAGIC{return Err("bad magic");}pos+=SZ_MAGIC;if rd_u8!(data,pos)!=VERSION{return Err("version mismatch");}
pos+=SZ_VER;let ulen=rd_u8!(data,pos)as usize;pos+=SZ_ULEN;if pos.saturating_add(ulen)>dlen{return Err("username overflow");}
let ubytes=rd_slice!(data,pos,ulen);let username=String::from_utf8(ubytes.to_vec()).map_err(|_|"invalid utf8")?;pos+=ulen;
chk!(pos,SZ_EXPIRY,dlen,"truncated expiry");let expiry:Timestamp=rd_i64!(data,pos);pos+=SZ_EXPIRY;chk!(pos,SZ_FLAGS,dlen,"truncated flags");
let flags:FeatureSet=rd_u16!(data,pos);pos+=SZ_FLAGS;if!validate_flags(flags){return Err("invalid flag combo");}chk!(pos,SZ_HASH,dlen,"truncated hash");
let stored=rd_slice!(data,pos,SZ_HASH);let computed=compute_hash(ubytes,expiry,flags);if!ct_cmp(stored,&computed){return Err("hash mismatch");}
Ok(LicenseInfo{username,expiry,flags,hash:computed.iter().map(|b|format!("{:02x}",b)).collect()})}
#[inline(always)]fn ct_cmp(a:&[u8],b:&[u8])->bool{if a.len()!=b.len(){return false;}let mut d=0u8;for i in 0..a.len(){d|=unsafe{
*a.get_unchecked(i)^*b.get_unchecked(i)};}d==0}
#[inline]fn compute_hash(u:&[u8],e:Timestamp,f:FeatureSet)->HashDigest{let mut buf=Vec::with_capacity(SALT.len()+u.len()+SZ_EXPIRY+SZ_FLAGS);
buf.extend_from_slice(SALT);buf.extend(xor_bytes(u,XOR_MASK));buf.extend_from_slice(&((e as u64).wrapping_mul(CKSUM_MULT)).to_le_bytes());
buf.extend_from_slice(&f.to_be_bytes());let mut h=Sha256::new();h.update(&buf);h.finalize().into()}
#[inline(never)]
fn banner(){
    println!("😭😭😭😭😭😢😢😢😢😢😢\n");
    println!("   ___   __  __ ___   ___  ___  ___    ");
    println!("  / _ | / / / // _ \\ / _ \\/ _ \\/ _ |   ");
    println!(" / __ |/ /_/ // , _// // / , _/ __ |   ");
    println!("/_/ |_|\\____//_/|_|/____/_/|_/_/ |_|   \n");
    println!("     LICENSE VALIDATOR v1.0\n");
}
#[inline(never)]
fn success(l:&LicenseInfo){
    println!("✨💖✨💖✨💖✨💖✨💖✨💖✨\n");
    println!("welcome back, diva");
    println!("vibe check passed ✨");
    println!("slay detected 💅");
    println!("you're so valid bestie 🌸\n");
    if has_flag(l.flags,FLAG_PREMIUM){println!("🌟 premium features unlocked");}
    if has_flag(l.flags,FLAG_ENTERPRISE){println!("🏢 enterprise edition active");}
    println!("\nyour flag: {}\n",l.hash);
    println!("✨💖✨💖✨💖✨💖✨💖✨💖✨");
}
#[inline(never)]#[cold]
fn fail()->!{
    println!("\n❌ gatekeeping intensifies 💅");
    println!("not on my watch, hun 🙅‍♀️");
    println!("the delusion is real 💀");
    println!("access DENIED periodt 🚫\n");
    process::exit(1);
}
fn main(){let args:Vec<String>=env::args().collect();if args.len()!=2{die!("usage: {} <license.auroralic>",args[0]);}let data=fs::read(&args[1]).unwrap_or_else(|e|
die!("read failed: {}",e));banner();match parse_license(&data){Ok(l)=>success(&l),Err(_)=>fail(),}}
