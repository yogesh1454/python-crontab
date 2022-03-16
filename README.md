## CronTab helper
https://crontab.guru/#*_*_*_*_*

# check your python version
> which python3

# Edit CronTab File
enter the crontab -e command to edit a cron file, or to make one if it doesn’t exist:
> crontab -e

# scheduler yor scipt for every 2 min
It will open a VIM editor — from there, click on the I key on your keyboard to enter insertion mode. You’ll have to specify the scheduling pattern, full path to the Python executable, and full path to the script to make scheduling work

```java
*/2 * * * * <python3 absolute path> <script absolute path>
```

# verify crontab changes
> crontab -l



