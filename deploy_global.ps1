# deploy_global.ps1
# Automates the promotion of workspace configurations to a machine-global Plugin

$GlobalPluginDir = "$env:USERPROFILE\.gemini\config\plugins\dev-healer"
$LocalWorkspace = "C:\Users\Johnny Cage\ITS"

Write-Output "=========================================================="
Write-Output "         DEVHEALER GLOBAL PLUGIN PROMOTION COMPILE        "
Write-Output "=========================================================="
Write-Output "[*] Sourcing local configuration from: $LocalWorkspace"
Write-Output "[*] Deploying machine-global plugin target: $GlobalPluginDir"

# Create directories
New-Item -ItemType Directory -Force -Path "$GlobalPluginDir\rules" | Out-Null
New-Item -ItemType Directory -Force -Path "$GlobalPluginDir\workflows" | Out-Null
New-Item -ItemType Directory -Force -Path "$GlobalPluginDir\skills\heal-and-evolve" | Out-Null
New-Item -ItemType Directory -Force -Path "$GlobalPluginDir\scripts" | Out-Null

# Write clean manifest plugin.json
$PluginJson = @{
    name = "dev-healer"
} | ConvertTo-Json
$PluginJson | Out-File -FilePath "$GlobalPluginDir\plugin.json" -Encoding utf8 -Force

# Write global hooks hooks.json pointing to absolute paths
$HooksJson = @{
    PreToolUse = @(
        @{
            command = "python"
            args = @("$GlobalPluginDir/scripts/pre-tool-use.py")
            timeout = 30
        }
    )
    PostToolUse = @(
        @{
            command = "python"
            args = @("$GlobalPluginDir/scripts/post-tool-use.py")
            timeout = 30
        }
    )
    Stop = @(
        @{
            command = "python"
            args = @("$GlobalPluginDir/scripts/stop-handler.py")
            timeout = 30
        }
    )
} | ConvertTo-Json -Depth 5
$HooksJson | Out-File -FilePath "$GlobalPluginDir\hooks.json" -Encoding utf8 -Force

# Copy supporting assets
Copy-Item -Force "$LocalWorkspace\.agents\rules\*" "$GlobalPluginDir\rules\\"
Copy-Item -Force "$LocalWorkspace\.agents\skills\heal-and-evolve\*" "$GlobalPluginDir\skills\heal-and-evolve\\"
Copy-Item -Force "$LocalWorkspace\scripts\*" "$GlobalPluginDir\scripts\\"
Copy-Item -Force "$LocalWorkspace\run_tests_hardened.py" "$GlobalPluginDir\scripts\\"

Write-Output "`n=========================================================="
Write-Output "  [+] SUCCESS: DevHealer Global Plugin Compiled & Deployed!"
Write-Output "  Ready across all independent workspaces!                "
Write-Output "=========================================================="
