@echo push
:start
cd /d "D:\D\PLACE TRAININGG\Day5"

git add.
git diff --cached --quiet
if %errorlevel%==0 (
    echo No changes to commit.
) else (
    git commit -m "Auto commit"
    git push origin main
)

timeout /t 10
goto start