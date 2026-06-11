from bnbagent import EVMWalletProvider
from eth_account import Account
import secrets

# Generiere einen privaten Schlüssel
private_key = "0x" + secrets.token_hex(32)
account = Account.from_key(private_key)

# Erstelle die Wallet mit Passwort (wie die Dokumentation es erwartet)
wallet = EVMWalletProvider(private_key=private_key, password="Bdelta4&multi&")

print("=== Deine neue Agent-Wallet ===")
print(f"Wallet-Adresse: {account.address}")
print(f"Privater Schlüssel: {private_key}")
print("\n⚠️ Bewahre den privaten Schlüssel sicher auf!")