import os
from dotenv import load_dotenv
from bnbagent import ERC8004Agent, AgentEndpoint, EVMWalletProvider

print("1. Lade .env Datei...")
load_dotenv()
print("   .env geladen")

print("2. Lade Wallet...")
wallet = EVMWalletProvider(
    password=os.getenv("WALLET_PASSWORD"),
    private_key=os.getenv("PRIVATE_KEY")
)
# print(f"   Wallet-Adresse: {wallet.get_address()}")

print("3. Verbinde mit BSC Testnet...")
sdk = ERC8004Agent(network="bsc-testnet", wallet_provider=wallet)
print("   Verbunden!")

print("4. Erstelle Agenten-Profil...")
agent_uri = sdk.generate_agent_uri(
    name="BNB-Hack-Agent",
    description="Autonomous Trading Agent für den BNB Hack 2026",
    endpoints=[
        AgentEndpoint(
            name="ERC-8183",
            endpoint="https://mein-agent.com/api",
            version="0.1.0",
        ),
    ],
)
print("   Profil erstellt!")

print("5. Registriere Agenten auf der Blockchain...")
result = sdk.register_agent(agent_uri=agent_uri)

print(f"\n✅ Agent erfolgreich registriert!")
print(f"🔢 Agent ID: {result['agentId']}")
print(f"🔗 Transaction: {result['transactionHash']}")