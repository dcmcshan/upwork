# iOS App Setup Guide

This guide will help you build and deploy the Upwork Browser iOS app using Capacitor.

## Prerequisites

- macOS (required for iOS development)
- Xcode 14 or later
- Node.js 18 or later
- npm or yarn

## Setup Steps

### 1. Install Dependencies

```bash
cd docs
npm install
npx cap init "Upwork Browser" com.dcmcshan.upwork
```

### 2. Add iOS Platform

```bash
npx cap add ios
```

### 3. Configure Info.plist

Edit `ios/App/App/Info.plist` to allow network connections:

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

### 4. Build the Web App

```bash
# The web files are already in docs/
# Capacitor will use them automatically
```

### 5. Sync with Capacitor

```bash
npx cap sync
```

### 6. Open in Xcode

```bash
npx cap open ios
```

### 7. Build and Run

In Xcode:
1. Select your device or simulator
2. Click the "Run" button (▶️)
3. The app will build and launch on your device

## Features

- **Upwork Browser**: Full web view of Upwork jobs
- **Cover Letter Generator**: Generate personalized cover letters
- **Share to App**: iOS share extension support
- **Native Feel**: Native iOS UI and gestures

## Customization

### Change Upwork URL

Edit `docs/index.html`:
```javascript
src="https://www.upwork.com/nx/search/jobs/"
```

### Change App Name

Edit `docs/capacitor.config.json`:
```json
"appName": "Your App Name"
```

### Change Bundle ID

Edit `docs/capacitor.config.json`:
```json
"appId": "com.yourcompany.yourapp"
```

## Distribution

### Ad Hoc Distribution

1. In Xcode, go to Product → Archive
2. Window → Organizer → Distribute App
3. Ad Hoc → Next
4. Select your provisioning profile
5. Export and share the .ipa file

### TestFlight

1. In Xcode, go to Product → Archive
2. Window → Organizer → Distribute App
3. App Store Connect → Next
4. Upload your app
5. Add testers and distribute

### Enterprise Distribution

1. Get an Enterprise distribution certificate
2. Archive and export with enterprise profile
3. Host the .ipa file on your server
4. Users install via web link

## Troubleshooting

### App won't build?
- Make sure Xcode is updated
- Clean build folder (Product → Clean Build Folder)
- Delete derived data

### Upwork doesn't load?
- Check Info.plist has NSAppTransportSecurity set
- Verify internet connection
- Try different Upwork URL

### Share extension not working?
- Add Share Extension target in Xcode
- Configure entitlements properly
- Test on real device

## Next Steps

1. Test on real iOS device
2. Add share extension for "Share to App"
3. Submit to App Store or distribute ad hoc
4. Update app regularly with new features

---

**Questions?** Check the Capacitor documentation or open an issue on GitHub.
