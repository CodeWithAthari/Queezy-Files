### build.gradle.kts (app)
```
plugins{
    ...
     id("com.google.gms.google-services")
    ...
}
...
android {
  ...

    defaultConfig {
    ...
      buildFeatures{
            viewBinding = true
        }
    ...
    }
    ...
}

...
dependencies {
     /*Firebase Libs*/
    implementation(platform(libs.firebase.bom))
    implementation(libs.firebase.analytics)
    implementation(libs.firebase.auth)
    implementation(libs.firebase.database)
    implementation(libs.firebase.storage)
    implementation(libs.firebase.firestore)

    /*Other libraries*/
    implementation (libs.glide)
    implementation (libs.otpview)
    implementation(libs.gson)
    implementation (libs.androidx.lifecycle.livedata.ktx)
}

```

### libs.toml (Queezy)
```
[versions]
# start external libs
firebaseBom = "33.0.0"
glide = "4.16.0"
lifecycleLivedataKtx = "2.7.0"
otpview = "3.1.0"
gson = "2.10.1"
# end external libs

[libraries]
# start external libs
firebase-bom = { module = "com.google.firebase:firebase-bom", version.ref = "firebaseBom" }
firebase-auth = { module = "com.google.firebase:firebase-auth-ktx"}
firebase-analytics = { module = "com.google.firebase:firebase-analytics-ktx"}
firebase-database = { module = "com.google.firebase:firebase-database-ktx"}
firebase-storage = { module = "com.google.firebase:firebase-storage-ktx"}
firebase-firestore = { module = "com.google.firebase:firebase-firestore-ktx"}
glide = { module = "com.github.bumptech.glide:glide", version.ref = "glide" }
otpview = { module = "com.github.mukeshsolanki.android-otpview-pinview:otpview", version.ref = "otpview" }
androidx-lifecycle-livedata-ktx = { module = "androidx.lifecycle:lifecycle-livedata-ktx", version.ref = "lifecycleLivedataKtx" }
gson = { module = "com.google.code.gson:gson", version.ref = "gson" }
# end external libs

```


### build.gradle.kts (Queezy)
```
// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    ...
    id("com.google.gms.google-services") version "4.4.1" apply false
}

```

### settings.gradle.kts (Queezy)
```
...
dependencyResolutionManagement {
   ...
    repositories {
        ...
        maven(url = "https://jitpack.io")
    ...
    }
    ...
}
...
```
