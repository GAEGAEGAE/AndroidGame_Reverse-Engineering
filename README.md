# AndroidGame_Reverse-Engineering

This tool can help generate frida script of tracing of Unity Games.

STEP1.
  Get Target game's method symbol and Save file 'methodSymbol.txt'
  
  [Example]
   
    public bool CanShowSkipLevel() { } // RVA: 0x5418EC Offset: 0x5418EC
	  public bool SpendGems(int nNo) { } // RVA: 0x5419E4 Offset: 0x5419E4
	  public void OnRewardOpened() { } // RVA: 0x541A14 Offset: 0x541A14
	  public void OnRewardx3() { } // RVA: 0x541BD4 Offset: 0x541BD4
	  public void SetDDReward() { } // RVA: 0x541D00 Offset: 0x541D00
	  public bool ShouldShowDailyReward() { } // RVA: 0x541D0C Offset: 0x541D0C
	  public int GetCurrentDayReward() { } // RVA: 0x541D14 Offset: 0x541D14
    
    
STEP2.
  Execute ScriptGenerate.py
  
  
STEP3.
  You can get output file 'scriptOutput.txt'.
  
  
  
  
