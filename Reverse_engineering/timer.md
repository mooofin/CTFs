# Reverse Engineering Timer APK



## Tools Used
- **JADX-GUI** (Java Decompiler) – To analyze the APK’s code.
- **APKTool** – For decompiling and inspecting resources.
- **AAPT (Android Asset Packaging Tool)** – To extract metadata.
- **AndroidManifest.xml** – Key file for identifying application metadata and permissions.

## Step 1: Decompiling the APK
The first step is to decompile the APK file using JADX-GUI or APKTool. This allows us to analyze the Java source code and configuration files.

```sh
jadx -d timer timer.apk
```

or using APKTool:

```sh
apktool d timer.apk -o timer_decompiled
```

## Step 2: Examining AndroidManifest.xml
The **AndroidManifest.xml** file contains essential metadata about the application, such as its package name, activities, and permissions. This file was inspected using JADX-GUI.

### Key Findings:
The **versionName** field contains the flag:

```xml
android:versionName="picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}"
```

### Full Manifest Extract:
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="1"
    android:versionName="picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}"
    android:compileSdkVersion="32"
    android:compileSdkVersionCodename="12"
    package="com.example.timer"
    platformBuildVersionCode="32"
    platformBuildVersionName="12">
    <uses-sdk
        android:minSdkVersion="21"
        android:targetSdkVersion="32"/>
    <application
        android:theme="@style/Theme.Timer"
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:debuggable="true"
        android:allowBackup="true"
        android:supportsRtl="true"
        android:fullBackupContent="@xml/backup_rules"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:appComponentFactory="androidx.core.app.CoreComponentFactory"
        android:dataExtractionRules="@xml/data_extraction_rules">
        <activity
            android:name="com.example.timer.MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <provider
            android:name="androidx.startup.InitializationProvider"
            android:exported="false"
            android:authorities="com.example.timer.androidx-startup">
            <meta-data
                android:name="androidx.emoji2.text.EmojiCompatInitializer"
                android:value="androidx.startup"/>
            <meta-data
                android:name="androidx.lifecycle.ProcessLifecycleInitializer"
                android:value="androidx.startup"/>
        </provider>
    </application>
</manifest>
```

## Step 3: Extracting the Flag
The **flag** is directly embedded in the **android:versionName** field:

```
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
```

