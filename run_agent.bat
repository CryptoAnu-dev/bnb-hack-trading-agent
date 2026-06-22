@echo off
cd C:\Users\nico9\Documents\bnb-hack-trading-agent
py pancake_trader.py >> logs.txt
echo %date% %time% - Agent ausgeführt >> logs.txt