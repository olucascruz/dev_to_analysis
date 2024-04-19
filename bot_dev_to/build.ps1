$exclude = @("venv", "bot_dev_to.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_dev_to.zip" -Force