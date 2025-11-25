```bash
remnux@remnux:~/muffin/Challenge_NotchItUp$ vol -f Challenge.raw imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/remnux/muffin/Challenge_NotchItUp/Challenge.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800027fa0a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800027fbd00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2019-08-19 14:41:58 UTC+0000
     Image local date and time : 2019-08-19 20:11:58 +0530

```

```bash
remnux@remnux:~/muffin/Challenge_NotchItUp$ vol -f Challenge.raw --profile=Win7SP1x64 pslist
Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa80012a5040 System                    4      0     78      495 ------      0 2019-08-19 14:40:07 UTC+0000                                 
0xfffffa8002971470 smss.exe                264      4      2       29 ------      0 2019-08-19 14:40:07 UTC+0000                                 
0xfffffa800234cb30 csrss.exe               336    328     10      415      0      0 2019-08-19 14:40:10 UTC+0000                                 
0xfffffa8002aae910 wininit.exe             384    328      3       74      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002ab7060 csrss.exe               396    376      9      499      1      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002b66560 winlogon.exe            436    376      6      116      1      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002b99200 services.exe            480    384      9      194      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002bb4600 lsass.exe               496    384      7      513      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa80022ff910 lsm.exe                 504    384     10      152      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002ce8740 svchost.exe             608    480     10      358      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002d13060 VBoxService.ex          668    480     13      136      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002d4bb30 svchost.exe             724    480      6      257      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002d4fb30 svchost.exe             780    480     19      405      0      0 2019-08-19 14:40:11 UTC+0000                                 
0xfffffa8002dcf5f0 svchost.exe             896    480     22      452      0      0 2019-08-19 14:40:12 UTC+0000                                 
0xfffffa8002de1b30 svchost.exe             948    480     35      893      0      0 2019-08-19 14:40:12 UTC+0000                                 
0xfffffa8002e0b1c0 audiodg.exe            1008    780      7      132      0      0 2019-08-19 14:40:12 UTC+0000                                 
0xfffffa8002e645f0 svchost.exe             400    480     13      275      0      0 2019-08-19 14:40:12 UTC+0000                                 
0xfffffa8002eac740 svchost.exe            1052    480     17      368      0      0 2019-08-19 14:40:12 UTC+0000                                 
0xfffffa8002e76b30 spoolsv.exe            1176    480     14      279      0      0 2019-08-19 14:40:13 UTC+0000                                 
0xfffffa8002f4d780 svchost.exe            1212    480     21      311      0      0 2019-08-19 14:40:13 UTC+0000                                 
0xfffffa8002f79b30 svchost.exe            1308    480     17      253      0      0 2019-08-19 14:40:13 UTC+0000                                 
0xfffffa8003144250 taskhost.exe           1812    480      9      147      1      0 2019-08-19 14:40:18 UTC+0000                                 
0xfffffa8003160120 dwm.exe                1868    896      4       70      1      0 2019-08-19 14:40:18 UTC+0000                                 
0xfffffa8003164b30 taskeng.exe            1876    948      5       81      0      0 2019-08-19 14:40:18 UTC+0000                                 
0xfffffa800319a060 explorer.exe           1944   1844     35      894      1      0 2019-08-19 14:40:19 UTC+0000                                 
0xfffffa8003227060 GoogleCrashHan         1292   1928      7      105      0      1 2019-08-19 14:40:19 UTC+0000                                 
0xfffffa8003219060 GoogleCrashHan          924   1928      6       93      0      0 2019-08-19 14:40:19 UTC+0000                                 
0xfffffa8003277810 VBoxTray.exe           1108   1944     14      139      1      0 2019-08-19 14:40:20 UTC+0000                                 
0xfffffa8002324b30 cmd.exe                 880   1944      1       21      1      0 2019-08-19 14:40:26 UTC+0000                                 
0xfffffa800231e370 conhost.exe             916    396      3       50      1      0 2019-08-19 14:40:26 UTC+0000                                 
0xfffffa8003315060 SearchIndexer.          856    480     13      689      0      0 2019-08-19 14:40:27 UTC+0000                                 
0xfffffa800234eb30 chrome.exe             2124   1944     27      662      1      0 2019-08-19 14:40:46 UTC+0000                                 
0xfffffa800234f780 chrome.exe             2132   2124      9       75      1      0 2019-08-19 14:40:46 UTC+0000                                 
0xfffffa800314fab0 chrome.exe             2168   2124      3       55      1      0 2019-08-19 14:40:49 UTC+0000                                 
0xfffffa80032d9060 WmiPrvSE.exe           2292    608     13      288      0      0 2019-08-19 14:40:52 UTC+0000                                 
0xfffffa80032f9a70 chrome.exe             2340   2124     12      282      1      0 2019-08-19 14:40:52 UTC+0000                                 
0xfffffa8003741b30 chrome.exe             2440   2124     13      263      1      0 2019-08-19 14:40:54 UTC+0000                                 
0xfffffa800374bb30 chrome.exe             2452   2124     14      167      1      0 2019-08-19 14:40:54 UTC+0000                                 
0xfffffa8002b74060 WmiApSrv.exe           2800    480      6      115      0      0 2019-08-19 14:40:57 UTC+0000                                 
0xfffffa8002d9eab0 WmiPrvSE.exe           2896    608      7      124      0      0 2019-08-19 14:40:57 UTC+0000                                 
0xfffffa80032d4380 chrome.exe             2940   2124      9      172      1      0 2019-08-19 14:41:06 UTC+0000                                 
0xfffffa8003905b30 firefox.exe            2080   3060     59      970      1      1 2019-08-19 14:41:08 UTC+0000                                 
0xfffffa80021fa630 firefox.exe            2860   2080     11      210      1      1 2019-08-19 14:41:09 UTC+0000                                 
0xfffffa80013a4580 firefox.exe            3016   2080     31      413      1      1 2019-08-19 14:41:10 UTC+0000                                 
0xfffffa8001415b30 firefox.exe            2968   2080     22      323      1      1 2019-08-19 14:41:11 UTC+0000                                 
0xfffffa8001454b30 firefox.exe            3316   2080     21      307      1      1 2019-08-19 14:41:13 UTC+0000                                 
0xfffffa80035e71e0 WinRAR.exe             3716   1944      7      201      1      0 2019-08-19 14:41:43 UTC+0000                                 
0xfffffa800156e400 DumpIt.exe             4084   1944      5       46      1      1 2019-08-19 14:41:55 UTC+0000                                 
0xfffffa80014c1060 conhost.exe            4092    396      2       50      1      0 2019-08-19 14:41:55 UTC+0000                                 
0xfffffa80014aa060 sppsvc.exe             1224    480      5        0 ------      0 2019-08-19 14:42:39 UTC+0000                                 
0xfffffa800157eb30 GoogleUpdate.e         2256   2396      3      118 ------      1 2019-08-19 14:42:40 UTC+0000                                 
0xfffffa80014f9060 GoogleCrashHan         1192   2256      3       46 ------      1 2019-08-19 14:42:41 UTC+0000                                 
0xfffffa80035e3700 GoogleCrashHan          864   2256      1 127...45      0      0 2019-08-19 14:42:41 UTC+0000
```

User activity was visible through explorer.exe, multiple Chrome processes so lets try that .


I found a cool repo with some plugins to extract the data from browsers :)

https://github.com/superponible/volatility-plugins
```
remnux@remnux:~/muffin$ volatility --plugins=/home/remnux/muffin/volatility-plugins -f /home/remnux/muffin/Challenge_NotchItUp/Challenge.raw --profile=Win7SP1x64 chromehistory
Volatility Foundation Volatility Framework 2.6.1
Index  URL                                                                              Title                                                                            Visits Typed Last Visit Time            Hidden Favicon ID
------ -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ------ ----- -------------------------- ------ ----------
   106 http://codechef.com/                                                             Programming Competition,Programming Contest,Online Computer Programming               1     1 2019-08-18 09:15:58.948446        N/A       
   105 https://leetcode.com/                                                            LeetCode - The World's Leading Online Programming Learning Platform                   1     1 2019-08-18 09:15:54.942315        N/A       
   103 http://codeforces.com/                                                           Codeforces                                                                            1     1 2019-08-18 09:15:29.107842        N/A       
    99 https://www.google.com/search?q=HTML5&s...cd2A20QxA0wGHoECA0QBw&biw=1920&bih=861 HTML5 - Google Search                                                                 1     0 2019-08-18 09:14:54.093016        N/A       
    92 https://www.google.com/search?q=python&...9i60.1327j0j7&sourceid=chrome&ie=UTF-8 python - Google Search                                                                1     0 2019-08-18 09:14:39.329069        N/A       
    91 https://www.google.com/search?q=bitbuck...j0l5.8221j0j7&sourceid=chrome&ie=UTF-8 bitbucket - Google Search                                                             1     0 2019-08-18 09:14:25.659572        N/A       
    89 https://gitlab.com/                                                              The first single application for the entire DevOps lifecycle - GitLab | GitLab        1     1 2019-08-18 09:14:19.989089        N/A       
    87 https://www.google.com/search?q=github+...60l3.2766j0j7&sourceid=chrome&ie=UTF-8 github students - Google Search                                                       1     0 2019-08-18 09:14:14.800350        N/A       
    74 https://www.google.com/search?q=xss&oq=...9i57.1231j0j7&sourceid=chrome&ie=UTF-8 xss - Google Search                                                                   1     0 2019-08-18 09:12:44.240215        N/A       
    73 https://www.google.com/search?q=google+...60l4.8083j0j7&sourceid=chrome&ie=UTF-8 google translate - Google Search                                                      1     0 2019-08-18 09:12:42.961712        N/A       
    60 https://github.com/                                                              The world’s leading software development platform · GitHub                         3     1 2019-08-18 10:34:35.472753        N/A       
    55 https://www.bbc.co.uk/                                                           BBC - Home                                                                            1     1 2019-08-18 09:02:16.190021        N/A       
    53 https://www.google.com/search?sa=X&q=MS...cHo8KHU2oC-MQ-BYIQjAy&biw=1920&bih=861 MSN - Google Search                                                                   1     0 2019-08-18 09:02:12.818539        N/A       
    52 https://www.google.com/search?q=CNN&sti...2sW4h4zkAhVdILkGHUB1DTgQxA0wGHoECA0QCw CNN - Google Search                                                                   1     0 2019-08-18 09:01:54.849209        N/A       
    49 https://www.google.com/search?q=google+....0l6.8360j0j7&sourceid=chrome&ie=UTF-8 google news - Google Search                                                           1     0 2019-08-18 09:01:46.562189        N/A       
    45 https://duckduckgo.com/                                                          DuckDuckGo — Privacy, simplified.                                                   3     2 2019-08-18 10:34:35.243136        N/A       
    39 https://instagram.com/                                                           Instagram                                                                             1     1 2019-08-18 08:59:28.284883        N/A       
    33 https://www.youtube.com/results?search_query=inctf                               inctf - YouTube                                                                       3     0 2019-08-18 08:56:23.824622        N/A       
    32 https://web.whatsapp.com/                                                        WhatsApp Web                                                                          3     2 2019-08-18 10:34:45.846048        N/A       
    26 https://www.bing.com/search?q=joseh+pri...&cvid=1ACB8D0FC45D4B56BB8E06D99F80CCB6 joseh priestley - Bing                                                                1     0 2019-08-18 08:51:33.551880        N/A       
    24 https://bing.com/                                                                Bing                                                                                  2     1 2019-08-18 10:34:35.118638        N/A       
    21 https://alibaba.com/                                                             Manufacturers, Suppliers, Exporters & I...est online B2B marketplace-Alibaba.com      2     1 2019-08-18 10:34:39.437200        N/A       
    19 https://www.google.com/search?q=sherloc...9i61.3097j0j7&sourceid=chrome&ie=UTF-8 sherlock holmes - Google Search                                                       1     0 2019-08-18 08:50:27.905256        N/A       
    18 https://www.google.com/search?q=james+b...j0l5.3661j0j7&sourceid=chrome&ie=UTF-8 james bond - Google Search                                                            1     0 2019-08-18 08:50:23.071895        N/A       
    17 https://www.google.com/search?q=john+wi...9i57.2080j0j7&sourceid=chrome&ie=UTF�N���NQ���                                                              1     0 1601-01-01 00:00:00               N/A       
    13 https://yahoo.com/                                                               Yahoo India                                                                           1     1 2019-08-18 08:49:47.398256        N/A       
    11 https://www.google.com/search?q=amazon&...j5l3.4623j0j7&sourceid=chrome&ie=UTF-8 amazon - Google Search                                                                1     0 2019-08-18 08:49:47.344713        N/A       
    10 https://twitter.com/                                                             Twitter. It's what's happening.                                                      12     3 2019-08-18 10:34:50.867782        N/A       
     7 https://facebook.com/                                                            Facebook – log in or sign up                                                        1     1 2019-08-18 08:49:31.612215        N/A       
     5 https://www.google.com/search?q=hello&o...9i57.1512j0j7&sourceid=chrome&ie=UTF-8 hello - Google Search                                                                 1     0 2019-08-18 08:49:07.715946        N/A       
     4 https://www.google.com/search?q=news&oq...69i57.629j0j7&sourceid=chrome&ie=UTF-8 news - Google Search                                                                  1     0 2019-08-18 08:49:07.645372        N/A       
     2 https://youtube.com/                                                             YouTube                                                                               3     2 2019-08-18 10:33:26.711730        N/A       
   192 https://filehippo.com/                                                           FileHippo.com - Download Free Software                                                1     1 2019-08-18 11:35:41.920761        N/A       
   180 https://gmail.com/                                                               Gmail - Free Storage and Email from Google                                            2     2 2019-08-18 10:58:42.307801        N/A       
   178 https://www.amrita.edu/                                                          Amrita Vishwa Vidyapeetham | Founded by Sri Mata Amritanandamayi Devi                 1     1 2019-08-18 10:33:47.158958        N/A       
   171 https://inctf.in/                                                                InCTF                                                                                 1     1 2019-08-18 10:32:37.603074        N/A       
   168 https://github.com/saransappa                                                    saransappa (Saran Sappa) · GitHub                                                    1     1 2019-08-18 09:22:15.086642        N/A       
   166 https://github.com/teambi0s                                                      Team bi0s · GitHub                                                                   1     1 2019-08-18 09:21:47.499262        N/A       
   164 https://volatilevirus.home.blog/                                                 Abhiram's Blog – Dying Is The Day Worth Living For!!                                1     1 2019-08-18 09:20:54.927065        N/A       
   162 https://bolisettynihith.wordpress.com/                                           Nihith's Blog                                                                         1     1 2019-08-18 09:20:42.747778        N/A       
   160 https://saransappa.wordpress.com/                                                Saran's Blog – A journey begins                                                     1     1 2019-08-18 09:20:23.132199        N/A       
   158 https://blog.bi0s.in/                                                            bi0s                                                                                  1     1 2019-08-18 09:20:02.448072        N/A       
   156 https://amfoss.in/                                                               India's Leading FOSS Club | FOSS@Amrita (amFOSS) - Code | Share | Grow                4     3 2019-08-18 10:34:23.871211        N/A       
   154 https://bi0s.in/                                                                 Amrita Bios                                                                           2     2 2019-08-18 10:32:45.490418        N/A       
   152 https://www.google.com/search?q=DELL&st...ZpBDL8QxA0wJHoECAsQBQ&biw=1920&bih=861 DELL - Google Search                                                                  1     0 2019-08-18 09:19:23.712377        N/A       
   150 https://www.google.com/search?tbm=isch&...UxnBQoQ4lYINSgG&biw=1920&bih=861&dpr=1 ferrari - Google Search                                                               1     0 2019-08-18 09:19:15.833318        N/A       
   147 https://www.google.com/search?q=ferrari...WX30KHdWyDbYQ_AUIESgB&biw=1920&bih=861 ferrari - Google Search                                                               1     0 2019-08-18 09:19:06.475805        N/A       
   146 https://www.google.com/search?q=bugatti...QIbcAHcHDDQsQ_AUIESgB&biw=1920&bih=861 bugatti - Google Search                                                               1     0 2019-08-18 09:19:02.664108        N/A       
   145 https://www.google.com/search?q=audi&so...o73MBHUmiBiwQ_AUIESgB&biw=1920&bih=861 audi - Google Search                                                                  1     0 2019-08-18 09:18:58.468379        N/A       
   144 https://www.google.com/search?q=mercede...WT30KHT3qB-4Q_AUIESgB&biw=1920&bih=861 mercedes - Google Search                                                              1     0 2019-08-18 09:18:52.872277        N/A       
   143 https://www.google.com/search?q=cars&so...ZT30KHYJuDHsQ_AUIESgB&biw=1920&bih=861 cars - Google Search                                                                  1     0 2019-08-18 09:18:49.335461        N/A       
   141 https://www.google.com/search?q=hp&oq=h...i60l3.675j0j7&sourceid=chrome&ie=UTF-8 hp - Google Search                                                                    1     0 2019-08-18 09:18:23.419136        N/A       
   140 https://www.google.com/search?q=ktm&oq=...i60l3.621j0j7&sourceid=chrome&ie=UTF-8 ktm - Google Search                                                                   1     0 2019-08-18 09:18:19.134012        N/A       
   139 https://www.google.com/search?q=ferrari...9i57.2171j0j7&sourceid=chrome&ie=UTF-8 ferrari - Google Search                                                               1     0 2019-08-18 09:18:16.994774        N/A       
   138 https://www.google.com/search?q=honda&o...60l3.1507j0j7&sourceid=chrome&ie=UTF-8 honda - Google Search                                                                 1     0 2019-08-18 09:18:11.907222        N/A       
   137 https://www.google.com/search?q=bugatti...9i61.1548j0j7&sourceid=chrome&ie=UTF-8 RW��PjWWP�u���{s�                                                               1     0 1601-01-01 00:00:00               N/A       
   136 https://www.google.com/search?q=audi&oq...9i58.3359j0j7&sourceid=chrome&ie=UTF-8 audi - Google Search                                                                  1     0 2019-08-18 09:17:59.971522        N/A       
   134 https://www.google.com/search?q=mercede...60l4.1477j0j7&sourceid=chrome&ie=UTF-8 mercedes - Google Search                                                              1     0 2019-08-18 09:17:49.664416        N/A       
   133 https://www.google.com/search?q=cars&oq...9i57.1393j0j7&sourceid=chrome&ie=UTF-8 cars - Google Search                                                                  1     0 2019-08-18 09:17:45.898424        N/A       
   115 https://topcoder.com/                                                            Design & Build High-Quality Software with Crowdsourcing | Topcoder                    1     1 2019-08-18 09:16:22.518791        N/A       
   113 https://www.google.com/search?q=coding+...j5l2.3789j0j7&sourceid=chrome&ie=UTF-8 coding is important - Google Search                                                   1     0 2019-08-18 09:16:21.028657        N/A       
   112 https://www.hackerearth.com/                                                     Trusted by recruiters across 1,000+ com...oved by 2.5M+ developers | HackerEarth      1     1 2019-08-18 09:16:16.951527        N/A       
   110 https://www.hackerrank.com/                                                      HackerRank                                                                            1     1 2019-08-18 09:16:04.703157        N/A       
   193 https://www.google.com/search?q=winrar+...j0l5.3724j0j7&sourceid=chrome&ie=UTF-8 winrar download - Google Search                                                       1     0 2019-08-18 11:36:03.768901        N/A       
   197 https://www.win-rar.com/postdownload.html?&L=0                                   WinRAR download and support: Post-Download                                            1     0 2019-08-18 11:36:45.122105        N/A       
   196 https://www.win-rar.com/predownload.html?&L=0                                    WinRAR download and support: Pre-Download                                             1     0 2019-08-18 11:36:35.848114        N/A       
   195 https://www.win-rar.com/download.html?&L=0                                       WinRAR download and support: Download                                                 1     0 2019-08-18 11:36:12.578033        N/A       
   194 https://www.win-rar.com/download.html                                            WinRAR download and support: Download                                                 1     0 2019-08-18 11:36:12.578033        N/A       
   191 http://filehippo.com/                                                            FileHippo.com - Download Free Software                                                1     0 2019-08-18 11:35:41.920761        N/A       
   190 https://accounts.google.com/signin/v2/i...e=GlifWebSignIn&flowEntry=ServiceLogin Gmail                                                                                 1     0 2019-08-18 10:58:55.398683        N/A       
   189 https://accounts.google.com/ServiceLogi...om%2Fmail%2F&service=mail&sacu=1&rip=1 Gmail                                                                                 2     0 2019-08-18 10:58:55.171386        N/A       
   188 https://accounts.google.com/AccountChoo...continue=https://mail.google.com/mail/ Gmail                                                                                 1     0 2019-08-18 10:58:53.750116        N/A       
   187 https://github.com/features/code-review/                                         Features · Code review · GitHub                                                     1     0 2019-08-18 10:35:47.914721        N/A       
   186 https://www.google.com/intl/en-GB/gmail/about/#                                  Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   185 https://www.google.com/intl/en-GB/mail/help/about.html#                          Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   184 https://mail.google.com/intl/en-GB/mail/help/about.html#                         Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   183 https://accounts.google.com/ServiceLogi...mpl=default&ltmplcache=2&emr=1&osid=1# Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   182 https://mail.google.com/mail/                                                    Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   181 https://www.google.com/gmail/                                                    Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   179 http://gmail.com/                                                                Gmail - Free Storage and Email from Google                                            2     0 2019-08-18 10:58:42.307801        N/A       
   177 http://amrita.edu/                                                               Amrita Vishwa Vidyapeetham | Founded by Sri Mata Amritanandamayi Devi                 1     0 2019-08-18 10:33:47.158958        N/A       
   176 https://bi0s.in/alumini.html                                                     Amrita Bios                                                                           1     0 2019-08-18 10:32:59.814353        N/A       
   175 https://bi0s.in/#contact                                                         Amrita Bios                                                                           1     0 2019-08-18 10:32:58.718865        N/A       
   174 https://bi0s.in/#events                                                          Amrita Bios                                                                           1     0 2019-08-18 10:32:57.167089        N/A       
   173 https://bi0s.in/#mentor                                                          Amrita Bios                                                                           1     0 2019-08-18 10:32:55.268243        N/A       
   172 https://bi0s.in/#expert                                                          Amrita Bios                                                                           1     0 2019-08-18 10:32:53.654828        N/A       
   170 http://inctf.in/                                                                 InCTF                                                                                 1     0 2019-08-18 10:32:37.603074        N/A       
   169 https://pastebin.com/RSGSi1hk                                                    Private Paste ID: RSGSi1hk                                                            1     0 2019-08-18 10:32:18.061245        N/A       
   167 http://github.com/saransappa                                                     saransappa (Saran Sappa) · GitHub                                                    1     0 2019-08-18 09:22:15.086642        N/A       
   165 http://github.com/teambi0s                                                       Team bi0s · GitHub                                                                   1     0 2019-08-18 09:21:47.499262        N/A       
   163 http://volatilevirus.home.blog/                                                  Abhiram's Blog – Dying Is The Day Worth Living For!!                                1     0 2019-08-18 09:20:54.927065        N/A       
   161 http://bolisettynihith.wordpress.com/                                            Nihith's Blog                                                                         1     0 2019-08-18 09:20:42.747778        N/A       
   159 http://saransappa.wordpress.com/                                                 Saran's Blog – A journey begins                                                     1     0 2019-08-18 09:20:23.132199        N/A       
   157 http://blog.bi0s.in/                                                             bi0s                                                                                  1     0 2019-08-18 09:20:02.448072        N/A       
   153 http://bi0s.in/                                                                  Amrita Bios                                                                           2     0 2019-08-18 10:32:45.490418        N/A       
   149 https://www.ferrari.com/en-IN                                                    Official Ferrari website                                                              2     0 2019-08-18 09:20:05.224275        N/A       
   155 http://amfoss.in/                                                                India's Leading FOSS Club | FOSS@Amrita (amFOSS) - Code | Share | Grow                4     0 2019-08-18 10:34:23.871211        N/A       
   151 https://en.wikipedia.org/wiki/KTM                                                KTM - Wikipedia                                                                       1     0 2019-08-18 09:19:22.092448        N/A       
   148 https://www.ferrari.com/                                                         Official Ferrari website                                                              1     0 2019-08-18 09:19:11.861563        N/A       
   137 https://www.google.com/search?q=bugatti...9i61.1548j0j7&sourceid=chrome&ie=UTF-8 bugatti - Google Search                                                               1     0 2019-08-18 09:18:05.177688        N/A       
   135 https://www.google.co.in/maps/@9.1000892,76.4909981,15z?hl=en                    Google Maps                                                                           4     0 2019-08-18 09:18:52.270220        N/A       
   132 https://www.google.co.in/maps?hl=en&tab=wl1                                      Google Maps                                                                           2     0 2019-08-18 09:17:46.151428        N/A       
   131 https://maps.google.co.in/maps?hl=en&tab=wl1                                     Google Maps                                                                           1     0 2019-08-18 09:17:22.196183        N/A       
   130 https://www.google.co.in/shopping?hl=en&source=og&tab=wf1                        Google Shopping - India                                                               1     0 2019-08-18 09:17:22.192965        N/A       
   129 https://support.google.com/websearch/?v...2079469831&hl=en-IN&rd=2#topic=3378866 Google Search Help                                                                    2     0 2019-08-18 09:17:20.407110        N/A       
   128 https://support.google.com/websearch/to..._id=637017165916966756-2079469831&rd=1 Google Search Help                                                                    1     0 2019-08-18 09:17:11.138537        N/A       
   127 https://support.google.com/websearch/?p=ws_results_help&hl=en-IN&fg=1            Google Search Help                                                                    1     0 2019-08-18 09:17:11.138537        N/A       
   126 https://www.spacesworks.com/the-importance-of-coding/                            What is Coding and Why is it so Important? - Spaces                                   1     0 2019-08-18 09:16:57.128771        N/A       
   125 https://www.quora.com/How-important-is-coding                                    How important is coding? - Quora                                                      1     0 2019-08-18 09:16:53.344818        N/A       
   124 http://blog.learningresources.com/5reasonskidscoding/                            5 Reasons why Coding is Important for Young Minds - Learning Resources Blog           1     0 2019-08-18 09:16:53.014393        N/A       
   123 https://www.tutorialspoint.com/videotutorials/index.htm                          Video Tutorials - Free Online Video Tutorials                                         1     0 2019-08-18 09:16:52.857877        N/A       
   122 https://store.tutorialspoint.com/                                                E-Books Store - TutorialsPoint                                                        1     0 2019-08-18 09:16:42.382746        N/A       
   121 https://www.w3schools.com/html/html_layout.asp                                   HTML Layouts                                                                          1     0 2019-08-18 09:16:42.258665        N/A       
   120 https://en.wikipedia.org/wiki/Category:Class-based_programming_languages         Category:Class-based programming languages - Wikipedia                                1     0 2019-08-18 09:16:36.310881        N/A       
   119 https://www.python.org/community/                                                Our Community | Python.org                                                            1     0 2019-08-18 09:16:26.602626        N/A       
   118 https://en.wikipedia.org/wiki/Python_(programming_language)#Mathematics          Python (programming language) - Wikipedia                                             1     0 2019-08-18 09:16:25.832035        N/A       
   117 https://www.topcoder.com/                                                        Design & Build High-Quality Software with Crowdsourcing | Topcoder                    1     0 2019-08-18 09:16:22.518791        N/A       
   116 http://www.topcoder.com/                                                         Design & Build High-Quality Software with Crowdsourcing | Topcoder                    1     0 2019-08-18 09:16:22.518791        N/A       
   114 http://topcoder.com/                                                             Design & Build High-Quality Software with Crowdsourcing | Topcoder                    1     0 2019-08-18 09:16:22.518791        N/A       
   111 http://hackerearth.com/                                                          Trusted by recruiters across 1,000+ com...oved by 2.5M+ developers | HackerEarth      1     0 2019-08-18 09:16:16.951527        N/A       
   109 http://hackerrank.com/                                                           HackerRank                                                                            1     0 2019-08-18 09:16:04.703157        N/A       
   108 https://www.codechef.com/                                                        Programming Competition,Programming Contest,Online Computer Programming               1     0 2019-08-18 09:15:58.948446        N/A       
   107 http://www.codechef.com/                                                         Programming Competition,Programming Contest,Online Computer Programming               1     0 2019-08-18 09:15:58.948446        N/A       
   104 http://leetcode.com/                                                             LeetCode - The World's Leading Online Programming Learning Platform                   1     0 2019-08-18 09:15:54.942315        N/A       
   102 https://www.w3.org/html/logo/                                                    W3C HTML5 Logo                                                                        1     0 2019-08-18 09:15:11.359770        N/A       
   101 https://www.w3schools.com/html/html5_intro.asp                                   HTML5 Introduction                                                                    1     0 2019-08-18 09:15:05.742457        N/A       
   100 https://www.tutorialspoint.com/python/index.htm                                  Python - Tutorial                                                                     1     0 2019-08-18 09:15:00.560123        N/A       
    98 https://en.wikipedia.org/wiki/Python_(programming_language)                      Python (programming language) - Wikipedia                                             1     0 2019-08-18 09:14:50.616361        N/A       
    97 https://www.python.org/                                                          Welcome to Python.org                                                                 1     0 2019-08-18 09:14:47.160836        N/A       
    96 https://bitbucket.org/product?&aceid=&a...2BVwKuEAAYASAAEgLr3PD_BwE&gclsrc=aw.ds Bitbucket | The Git solution for professional teams                                   1     0 2019-08-18 09:14:40.063327        N/A       
    95 https://ad.doubleclick.net/ddm/clk/3197...2BVwKuEAAYASAAEgLr3PD_BwE&gclsrc=aw.ds Bitbucket | The Git solution for professional teams                                   1     0 2019-08-18 09:14:40.063327        N/A       
    73 https://www.google.com/search?q=google+...�                                                       1     0 1601-01-01 00:00:00               N/A       
    93 https://www.googleadservices.com/pagead...iozkAhXgGbkGHSbrCpoQ0Qx6BAgMEAE&adurl= Bitbucket | The Git solution for professional teams                                   1     0 2019-08-18 09:14:40.063327        N/A       
    83 https://translate.google.com/intl/en/about/                                      Google Translate - A Personal Interpreter on Your Phone or Computer                   1     0 2019-08-18 09:13:48.421514        N/A       
    82 https://www.spotify.com/in/about-us/contact/                                     Contact - Spotify                                                                     1     0 2019-08-18 09:13:33.199409        N/A       
    81 https://developer.spotify.com/?_ga=2.90...506848.1566119549-848351807.1566119549 Home | Spotify for Developers                                                         1     0 2019-08-18 09:13:32.120118        N/A       
    80 https://accounts.spotify.com/login/?con...com/in/account/overview/&_locale=en-IN Spotify                                                                               1     0 2019-08-18 09:13:30.810821        N/A       
    79 https://www.spotify.com/in/login/                                                Spotify                                                                               1     0 2019-08-18 09:13:30.810821        N/A       
    78 https://en.wikipedia.org/wiki/Vulnerability_(computing)                          Vulnerability (computing) - Wikipedia                                                 1     0 2019-08-18 09:13:14.112244        N/A       
    77 https://en.wikipedia.org/wiki/Vulnerability_(computer_science)                   Vulnerability (computing) - Wikipedia                                                 1     0 2019-08-18 09:13:13.120782        N/A       
    94 https://clickserve.dartsearch.net/link/...oqM5AIVjoKRCh2BVwKuEAAYASAAEgLr3PD_BwE Bitbucket | The Git solution for professional teams                                   1     0 2019-08-18 09:14:40.063327        N/A       
    90 https://about.gitlab.com/                                                        The first single application for the entire DevOps lifecycle - GitLab | GitLab        1     0 2019-08-18 09:14:19.989089        N/A       
    88 http://gitlab.com/                                                               The first single application for the entire DevOps lifecycle - GitLab | GitLab        1     0 2019-08-18 09:14:19.989089        N/A       
    86 https://accounts.spotify.com/en/login/?...%2Faccount%2Foverview%2F&_locale=en-IN Login - Spotify                                                                       1     0 2019-08-18 09:13:55.774103        N/A       
    85 https://accounts.spotify.com/login/?con...%2Faccount%2Foverview%2F&_locale=en-IN Login - Spotify                                                                       1     0 2019-08-18 09:13:55.650365        N/A       
    84 https://www.theatlantic.com/technology/...hallowness-of-google-translate/551570/ The Shallowness of Google Translate - The Atlantic                                    1     0 2019-08-18 09:13:51.859084        N/A       
    20 http://alibaba.com/                                                              Manufacturers, Suppliers, Exporters & I...est online B2B marketplace-Alibaba.com      2     0 2019-08-18 10:34:39.437200        N/A       
    23 http://bing.com/                                                                 Bing                                                                                  2     0 2019-08-18 10:34:35.118638        N/A       
    40 https://www.instagram.com/                                                       Instagram                                                                             2     0 2019-08-18 08:59:30.987715        N/A       
    38 http://instagram.com/                                                            Instagram                                                                             1     0 2019-08-18 08:59:28.284883        N/A       
    37 https://www.youtube.com/watch?v=Hp_YVg5QFEw                                      Introduction to Binary Exploitation - YouTube                                         1     0 2019-08-18 08:57:55.499962        N/A       
    36 https://www.youtube.com/watch?v=jZoDRzBDeHY                                      Basic Data Structures in C - YouTube                                                  3     0 2019-08-18 08:58:53.431878        N/A       
    35 https://www.youtube.com/watch?v=rpbBlb1KcrI                                      YouTube                                                                               1     0 2019-08-18 08:57:03.482634        N/A       
    34 https://www.youtube.com/channel/UC2upioDqOCMYnGvgJw7iOMA                         Amrita InCTF Junior - YouTube                                                         2     0 2019-08-18 08:58:53.435974        N/A       
    30 https://en.wikipedia.org/wiki/Joseph_Priestley                                   Joseph Priestley - Wikipedia                                                          1     0 2019-08-18 08:54:19.909075        N/A       
    29 https://www.alibaba.com/Consumer-Electr...=a2700.8293689.201703.1.2ce265aaGiA0pM Consumer Electronics Market                                                           1     0 2019-08-18 08:53:06.450328        N/A       
    28 https://developer.twitter.com/                                                   Developer — Twitter Developers                                                      1     0 2019-08-18 08:59:16.884610        N/A       
    27 https://dev.twitter.com/                                                         Developer — Twitter Developers                                                      1     0 2019-08-18 08:52:40.588035        N/A       
    25 https://www.bing.com/?toWww=1&redig=B9C0383E335545958632975F8276805F             Bing                                                                                  2     0 2019-08-18 10:34:35.118638        N/A       
    31 http://web.whatsapp.com/                                                         WhatsApp Web                                                                          3     0 2019-08-18 10:34:45.846048        N/A       
    22 https://www.alibaba.com/                                                         Manufacturers, Suppliers, Exporters & I...est online B2B marketplace-Alibaba.com      2     0 2019-08-18 10:34:39.437200        N/A       
    17 https://www.google.com/search?q=john+wi...9i57.2080j0j7&sourceid=chrome&ie=UTF-8 john wik - Google Search                                                              1     0 2019-08-18 08:50:18.587651        N/A       
    16 https://www.indiatoday.in/news.html                                              News - Breaking News, Latest News & Top Video News                                    1     0 2019-08-18 08:49:58.577513        N/A       
    15 https://in.yahoo.com/?p=us                                                       Yahoo India                                                                           3     0 2019-08-18 08:55:10.814539        N/A       
    14 https://www.yahoo.com/                                                           Yahoo India                                                                           1     0 2019-08-18 08:49:47.398256        N/A       
    12 http://yahoo.com/                                                                Yahoo India                                                                           1     0 2019-08-18 08:49:47.398256        N/A       
     9 http://twitter.com/                                                              Twitter. It's what's happening.                                                       1     0 2019-08-18 08:49:37.103125        N/A       
     8 https://www.facebook.com/                                                        Facebook – log in or sign up                                                        2     0 2019-08-18 08:51:39.103458        N/A       
     6 http://facebook.com/                                                             Facebook – log in or sign up                                                        1     0 2019-08-18 08:49:31.612215        N/A       
     3 https://www.youtube.com/                                                         YouTube                                                                               3     0 2019-08-18 10:33:26.711730        N/A       
     1 http://youtube.com/                                                              YouTube                                                                               3     0 2019-08-18 10:33:26.711730        N/A       
    59 http://github.com/                                                               The world’s leading software development platform · GitHub                         3     0 2019-08-18 10:34:35.472753        N/A       
    44 http://duckduckgo.com/                                                           DuckDuckGo — Privacy, simplified.                                                   3     0 2019-08-18 10:34:35.243136        N/A       
    43 https://www.instagram.com/directory/hashtags/3-5/                                Hashtags • Instagram                                                                2     0 2019-08-18 09:00:05.905419        N/A       
    42 https://www.instagram.com/directory/hashtags/3/                                  Hashtags • Instagram                                                                2     0 2019-08-18 08:59:56.232944        N/A       
    41 https://www.instagram.com/directory/hashtags/                                    Hashtags • Instagram                                                                2     0 2019-08-18 08:59:39.384654        N/A       
    76 https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)                       Cross-site Scripting (XSS) - OWASP                                                    1     0 2019-08-18 09:12:51.592160        N/A       
    75 https://en.wikipedia.org/wiki/Cross-site_scripting                               Cross-site scripting - Wikipedia                                                      1     0 2019-08-18 09:12:49.696658        N/A       
    72 https://www.spotify.com/in/                                                      Music for everyone - Spotify                                                          1     0 2019-08-18 09:12:20.436643        N/A       
    71 https://www.spotify.com/                                                         Music for everyone - Spotify                                                          1     0 2019-08-18 09:12:20.436643        N/A       
    70 http://spotify.com/                                                              Music for everyone - Spotify                                                          1     0 2019-08-18 09:12:20.436643        N/A       
    67 https://www.google.com/url?q=https://do...usg=AFQjCNGEFaqVLhdojKu_HzaoS5Pq30Ba-w Redirecting                                                                           1     0 2019-08-18 09:11:23.131684        N/A       
    66 https://www.virustotal.com/gui/home/upload                                       VirusTotal                                                                            1     0 2019-08-18 09:10:43.332064        N/A       
    65 https://www.virustotal.com/gui/home                                              VirusTotal                                                                            1     0 2019-08-18 09:10:39.599065        N/A       
    64 https://www.virustotal.com/gui/                                                  VirusTotal                                                                            1     0 2019-08-18 09:10:27.054942        N/A       
    63 https://virustotal.com/                                                          VirusTotal                                                                            1     0 2019-08-18 09:10:27.054942        N/A       
    62 http://virustotal.com/                                                           VirusTotal                                                                            1     0 2019-08-18 09:10:27.054942        N/A       
    61 https://enterprise.github.com/contact                                            Contact us - GitHub Enterprise                                                        1     0 2019-08-18 09:04:04.570918        N/A       
    58 https://www.bbc.co.uk/programmes/n3ct6kjw                                        BBC World News - Panorama, Boeing's Killer Planes                                     1     0 2019-08-18 09:03:01.668305        N/A       
    57 https://www.bbc.co.uk/schedules/p00fzl9m                                         BBC WORLD NEWS North America - Schedules                                              1     0 2019-08-18 09:03:01.360682        N/A       
    56 https://www.bbc.com/cymru                                                        BBC - Cymru - Hafan                                                                   1     0 2019-08-18 09:02:48.507498        N/A       
    54 http://bbc.co.uk/                                                                BBC - Home                                                                            1     0 2019-08-18 09:02:16.190021        N/A       
    51 https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en                               Google News                                                                           3     0 2019-08-18 09:02:09.000277        N/A       
    50 https://news.google.co.in/                                                       Google News                                                                           1     0 2019-08-18 09:01:53.994599        N/A       
    48 https://duckduckgo.com/about                                                     About DuckDuckGo                                                                      1     0 2019-08-18 09:01:29.038955        N/A       
    47 https://duckduckgo.com/spread                                                    Help Spread DuckDuckGo                                                                1     0 2019-08-18 09:01:16.166387        N/A       
    46 https://start.duckduckgo.com/                                                    DuckDuckGo — Privacy, simplified.                                                   1     0 2019-08-18 09:00:43.840423        N/A       
   164 https://volatilevirus.homNTEGER                                                  NOT NULL,is_httponly INTEGER NOT NULL,last_access_utc  
```

From the output i spotted a pastebin entry !



* **Index:** 169
* **URL:** `https://pastebin.com/RSGSi1hk`
* **Title:** Private Paste ID: RSGSi1hk
* **Last Visit:** 2019-08-18 10:32:18 UTC


<img width="1355" height="545" alt="image" src="https://github.com/user-attachments/assets/23d91803-7134-45c2-9615-4dae20a30048" />

It redirected me to a website that had a encrypted data ; 


<img width="1918" height="762" alt="image" src="https://github.com/user-attachments/assets/dc8a136a-0acd-4eff-84a7-51a19e49a9b3" />


Then runnings strings gave the key 

strings Challenge.raw | grep "Mega Drive Key"

<img width="1920" height="913" alt="Screenshot from 2025-11-25 15-21-08" src="https://github.com/user-attachments/assets/bf043e2d-1170-4c4f-b428-ea0cacf096ba" />

After entering the key i got the flag :) 
[the file was corrupted but i fixed it ] 

 inctf{thi5_cH4LL3Ng3_!s_g0nn4_b3_?


<img width="1920" height="913" alt="Screenshot from 2025-11-25 15-25-50" src="https://github.com/user-attachments/assets/f54109e6-4565-4f9b-83b8-08d4b14f2c98" />

 Running envars after trying some more plugins gave a rar key ? So we need to dump what was zipped and use this to exctract it 


