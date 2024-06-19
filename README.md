Step Menjalankan Testing
1. Jalankan Emulator Android AVD (Android Virtual Device)
2. Aktifkan server Appium menggunakan appium --allow-cors
3. Start session pada Appium server dengan ketentuan Capability Set

    {
      "platformName": "Android",
      "appium:platformVersion": "11",
      "appium:deviceName": "emulator-5554",
      "appium:app": "C:\\Users\\User\\Downloads\\Wattpad - Read & Write Stories_10.66.0_APKPure.apk",
      "appium:automationName": "UiAutomator2",
      "appium:ensureWebviewsHavePages": "true"
    }
4. Run file yang berisikan code testing


Link Spredsheet UAS Automation Testing
https://docs.google.com/spreadsheets/d/1y12QS2Su1hSTbIfNAeKK3gJS2vuS4trKpn45QwVNRGU/edit?usp=sharing