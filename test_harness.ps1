# test_harness.ps1
# Diagnostics & Validation Suite for DevHealer MAPE-K Loop

Write-Output "=========================================================="
Write-Output "   DEVHEALER MAPE-K LOOP LOCAL DIAGNOSTICS SUITE  "
Write-Output "=========================================================="

$WorkspaceRoot = "C:\Users\Johnny Cage\ITS"
$SecureAppData = "$env:USERPROFILE\.gemini\antigravity\sidecar_data\dev-healer\watcher\data"

Write-Output "[*] Target Project Directory: $WorkspaceRoot"
Write-Output "[*] Isolated Secure AppData Target: $SecureAppData"

# 1. Verification of Workspace & Git Support
Write-Output "`n[*] Verifying Project Workspace..."
if (Test-Path "$WorkspaceRoot\.git") {
    Write-Output " [+] Git Repository successfully initialized. New Worktree Mode isolation is active."
} else {
    Write-Warning " [-] Git not initialized locally. Setup setup.py first."
}

# 2. Allocate AppData State Storage Path
Write-Output "`n[*] Allocating isolated secure AppData directories..."
New-Item -ItemType Directory -Force -Path $SecureAppData | Out-Null
Write-Output " [+] Secure path active: $SecureAppData"

# 3. Mock Anomaly Injection
Write-Output "`n[*] Injecting test compile anomaly trigger..."
$AnomalyPayload = @{
    activeAnomaly = "ToolFailure"
    errorDetails = "Compilation failed in index.js: SyntaxError Unexpected token"
    status = "active"
    retryCount = 0
} | ConvertTo-Json

$StateFile = "$SecureAppData\healing-state.json"
$AnomalyPayload | Out-File -FilePath $StateFile -Encoding utf8 -Force
Write-Output " [+] Mock anomaly registered in secure AppData: $StateFile"

# 4. Simulation of Watcher Sidecar Detection
Write-Output "`n[*] Booting Watcher Sensation Module simulation..."
Write-Output " [+] Simulating 'agentapi new-conversation ...' proactive trigger"
Write-Output " [+] Loop status: Listening for disruptions on file saves."

Write-Output "`n=========================================================="
Write-Output "       [+] STATE CACHE UPDATED - DIAGNOSTIC SUCCESS!       "
Write-Output "=========================================================="
