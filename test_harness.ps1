<#
.SYNOPSIS
    PowerShell Test Script for Google Antigravity 2.0 Self-Healer Sidecar and Hooks.
    Tailored for Windows 10: C:\Users\Johnny Cage\ITS
#>

$ProjectRoot = "C:\Users\Johnny Cage\ITS"
$GeminiDir = "$env:USERPROFILE\.gemini"
$SidecarId = "antigravity-self-healer/watcher"
$StateDir = "$GeminiDir\antigravity\sidecar_data\$SidecarId\data"
$StateFile = "$StateDir\healing-state.json"
$TriggerFile = "$ProjectRoot\trigger_error.txt"

Clear-Host
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "     GOOGLE ANTIGRAVITY 2.0 - SELF-HEALER DIAGNOSTIC TOOL (WINDOWS)  " -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Environment & Path Verification
Write-Host "[*] Verifying path layouts..." -ForegroundColor Yellow
if (-not (Test-Path $ProjectRoot)) {
    Write-Error "Workspace path not found: $ProjectRoot. Please run setup_dev_healer_v5.py first."
    Exit
}
Write-Host "  [+] Active Workspace found: $ProjectRoot" -ForegroundColor Green

# Verify Git is initialized
Set-Location $ProjectRoot
$isGit = git rev-parse --is-inside-work-tree 2>$null
if ($lastExitCode -ne 0) {
    Write-Warning "  [!] Git is not yet active in this workspace. Run the setup script to initialize Git, ensuring Worktree isolation functions."
} else {
    Write-Host "  [+] Git is active. Ready for isolated background worktree execution." -ForegroundColor Green
}

# 2. Check for AppData Isolation Paths
Write-Host ""
Write-Host "[*] Verifying system-allocated AppData paths..." -ForegroundColor Yellow
if (-not (Test-Path $StateDir)) {
    Write-Host "  [*] Creating system-allocated state folder to match ANTIGRAVITY_EXECUTABLE_DATA_DIR..." -ForegroundColor Gray
    New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
}
Write-Host "  [+] Secure state folder verified at: $StateDir" -ForegroundColor Green

# 3. Simulate a Compilation Failure Anomaly
Write-Host ""
Write-Host "[*] Simulating project anomaly..." -ForegroundColor Yellow
$MockErrorMessage = "Compilation failed in auth_service.py: NameError 'client_reference_id' is not defined"
Write-Host "  --> Writing mock compilation failure to $TriggerFile..." -ForegroundColor Gray
$MockErrorMessage | Out-File -FilePath $TriggerFile -Encoding utf8

# 4. Trigger Sidecar Monitoring Log Logic
Write-Host ""
Write-Host "[*] Activating watcher parsing logic..." -ForegroundColor Yellow
# Run the watcher module on a single-pass mock execution
$WatcherScript = "$ProjectRoot\sidecars\watcher\watcher.py"
if (Test-Path $WatcherScript) {
    Write-Host "  --> Executing Python watcher loop on your local Python interpreter..." -ForegroundColor Gray
    # Force python to run the watcher once (mocked environment setup)
    $env:ANTIGRAVITY_EXECUTABLE_DATA_DIR = $StateDir
    $env:PROJECT_ID = "test-windows-project-id"
    python $WatcherScript --one-run
    
    # Check if watcher wrote the anomaly to the secure data cache
    if (Test-Path $StateFile) {
        Write-Host "  [+] STATE CACHE UPDATED!" -ForegroundColor Green
        Write-Host "  Reading logged anomaly state from: $StateFile" -ForegroundColor Gray
        Get-Content $StateFile | ConvertFrom-Json | Format-List
    } else {
        Write-Warning "  [!] State file was not generated at $StateFile. Ensure write permissions are granted."
    }
} else {
    Write-Warning "  [!] watcher.py script not found at $WatcherScript. Run setup_dev_healer_v5.py first."
}

# 5. Clean up simulated files
Write-Host ""
Write-Host "[*] Clean up simulated workspace files..." -ForegroundColor Yellow
if (Test-Path $TriggerFile) {
    Remove-Item $TriggerFile -Force
    Write-Host "  [+] Removed trigger_error.txt" -ForegroundColor Green
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  DIAGNOSTICS COMPLETED. Drop the script into your Windows PowerShell " -ForegroundColor Cyan
Write-Host "  terminal in 'C:\Users\Johnny Cage\ITS' to run active verifications! " -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
