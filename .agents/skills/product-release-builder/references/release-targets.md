# Release Target Discovery

Inspect project manifests and artifacts, then show only credible targets.

| Target | Typical evidence | Packaging result |
| --- | --- | --- |
| Web service or site | web framework, routes, build script | deploy bundle and deployment instructions |
| Desktop application | Electron, Tauri, native project | signed or unsigned installer/package |
| Mobile application | Android/iOS project | APK/AAB or archive/build result |
| CLI | executable entry point and command tests | archive, installer, or package registry artifact |
| Library/package | public API and package manifest | registry-ready archive |
| Container | service entry point and container config | image digest and run verification |
| Static artifact | generated files without runtime service | versioned archive and checksums |

After discovery, ask the user to select one target. Do not infer permission to publish externally.
