#!/usr/bin/env julia

using SHA

const MAGIC_BYTES = b"AUR0"
const LICENSE_VERSION = 0x01
const XOR_KEY = 0x42
const CHECKSUM_MULTIPLIER = 0x5f3759df
const VALIDATION_SEED = b"aurora_ctf_2025_secret_salt"

function generate_license(username::String, expiry_timestamp::Int64, feature_flags::UInt16, output_file::String)
    data_to_hash = UInt8[]
    append!(data_to_hash, VALIDATION_SEED)
    
    username_bytes = Vector{UInt8}(username)
    for byte in username_bytes
        push!(data_to_hash, byte ⊻ XOR_KEY)
    end
    
    mixed_timestamp = UInt64(expiry_timestamp) * UInt64(CHECKSUM_MULTIPLIER)
    append!(data_to_hash, reinterpret(UInt8, [htol(mixed_timestamp)]))
    
    feature_flags_be = hton(feature_flags)
    append!(data_to_hash, reinterpret(UInt8, [feature_flags_be]))
    
    checksum = sha256(data_to_hash)
    
    license_data = vcat(
        collect(MAGIC_BYTES),
        [LICENSE_VERSION],
        [UInt8(length(username_bytes))],
        username_bytes,
        reinterpret(UInt8, [hton(UInt64(expiry_timestamp))]),
        reinterpret(UInt8, [feature_flags_be]),
        checksum
    )
    
    write(output_file, license_data)
end

function main()
    length(ARGS) == 4 || (println("Usage: julia keygen.jl <username> <expiry> <features> <output>"); exit(1))
    
    username = ARGS[1]
    expiry = parse(Int64, ARGS[2])
    features = startswith(ARGS[3], "0x") ? parse(UInt16, ARGS[3][3:end], base=16) : parse(UInt16, ARGS[3])
    output = ARGS[4]
    
    generate_license(username, expiry, features, output)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
