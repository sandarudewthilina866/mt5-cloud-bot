import MetaTrader5 as mt5
import time

# --- ⚠️ උඹේ Deriv විස්තර සියල්ලම මෙතනට ඇතුළත් කර ඇත ---
MT5_LOGIN = 6187001
MT5_PASSWORD = "_4!qxb_iBAXSwq7"
MT5_SERVER = "Deriv-Demo"
# -------------------------------------------------------------

def initialize_mt5():
    print("සර්වර් එකට සම්බන්ධ වීමට උත්සාහ කරයි...")
    
    # MT5 ප්ලැට්ෆෝම් එක Cloud එකේ ස්ටාර්ට් කිරීම
    if not mt5.initialize():
        print("MT5 initialize() failed, error code =", mt5.last_error())
        quit()
    
    # ලබාදුන් විස්තර මගින් Deriv සර්වර් එකට ලොග් වීම
    authorized = mt5.login(MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
    if authorized:
        print("✅ MT5 සර්වර් එකට සාර්ථකව සම්බන්ධ වුණා!")
        account_info = mt5.account_info()
        if account_info is not None:
            print(f"Account Balance: {account_info.balance} | Currency: {account_info.currency}")
    else:
        print(f"❌ ලොග් වෙන්න බැරි වුණා. Error code: {mt5.last_error()}")
        mt5.shutdown()
        quit()

def check_market_and_trade():
    # Deriv Financial එකවුන්ට් එකක් නිසා අපි බහුලව ට්‍රේඩ් කරන EURUSD යුගලය පාවිච්චි කරමු
    symbol = "EURUSD" 
    
    while True:
        # මාකට් එකෙන් අලුත්ම මිල ගණන් (Ticks) ලබාගැනීම
        tick = mt5.symbol_info_tick(symbol)
        if tick:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {symbol} -> Ask: {tick.ask} | Bid: {tick.bid}")
            
            # 💡 උඹේ බොට්ගේ Trading Logic එක (RSI, Moving Average ආදී) මීට පල්ලෙහායින් ඇතුළත් කරන්න පුළුවන්.
            # ( දැනට මේකෙන් කරන්නේ මාකට් ප්‍රයිස් එක හැම විනාඩියකම ලොග් එකේ ප්‍රින්ට් කරන එක විතරයි )
            
        else:
            print(f"සැලකිල්ලට ගන්න: {symbol} සඳහා මිල ගණන් ලබාගත නොහැක. සර්වර් සම්බන්ධතාවය පරීක්ෂා කරන්න.")

        # හැම තත්පර 60කට වරක්ම මාකට් එක චෙක් කරනවා (ඩේටා සහ මෙමරි ඉතිරි කරගැනීමට)
        time.sleep(60) 

if __name__ == "__main__":
    print("=== Cloud MT5 Bot Script Started ===")
    initialize_mt5()
    
    try:
        check_market_and_trade()
    except KeyboardInterrupt:
        print("බොට් ක්‍රියාවලිය පරිශීලකයා විසින් නවත්වන ලදී.")
    finally:
        mt5.shutdown()
        print("MT5 කනෙක්ෂන් එක වසා දමන ලදී.")
