from scripts.helpful_scripts import get_account
from brownie import interface, config, network, accounts
import sys


def main():
    get_weth()

def get_weth():
    """
    Mint some Weth
    """
    account = get_account()
    weth = interface.IWeth(config["network"[network.show_active()]["weth_token"]])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("received 0.1 weth")
