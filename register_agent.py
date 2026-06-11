import os
from dotenv import load_dotenv
from bnbagent import ERC8004Agent, AgentEndpoint, EVMWalletProvider

load_dotenv()

# 1. Wallet laden (diesmal mit deinem privaten Schlüssel)
wallet = EVMWalletProvider(
    password=os.getenv("WALLET_PASSWORD"),
    private_key=os.getenv("PRIVATE_KEY")
)

# 2. Verbindung zum BSC Testnet herstellen
sdk = ERC8004Agent(network="bsc-testnet", wallet_provider=wallet)

# 3. Agenten-Profil erstellen (wichtig für die Jury!)
agent_uri = sdk.generate_agent_uri(
    name="BNB-Hack-Agent",
    description="Autonomous Trading Agent für den BNB Hack 2026 – nutzt CMC Daten und TWAK für Ausführung.",
    endpoints=[
        AgentEndpoint(
            name="ERC-8183",
            endpoint="https://mein-agent.com/api", # Hier später deine echte Endpoint-URL
            version="0.1.0",
        ),
    ],
)

# 4. Registrierung durchführen (gas-frei dank MegaFuel Paymaster auf Testnet!)
result = sdk.register_agent(agent_uri=agent_uri)

print(f"✅ Agent erfolgreich registriert!")
print(f"🔢 Agent ID: {result['agentId']}")
print(f"🔗 Transaction: {result['transactionHash']}")