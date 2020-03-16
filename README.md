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
  
  [Example]
  	// public bool CanShowSkipLevel() { } // RVA: 0x5418EC Offset: 0x5418EC

var offset = 0x5418EC;
var CanShowSkipLevel = il2cpp.add(offset);

Interceptor.attach(CanShowSkipLevel,
{
    onEnter: function(args)
    {
        console.log("[+] CanShowSkipLevel Hook onEnter()");
        console.log("    args[0] : " + args[0]);
    },
    onLeave: function(retVal)
    {
        console.log("    retVal : " + retVal);
        console.log("");
    }
});



// public bool SpendGems(int nNo) { } // RVA: 0x5419E4 Offset: 0x5419E4

var offset = 0x5419E4;
var SpendGems = il2cpp.add(offset);

Interceptor.attach(SpendGems,
{
    onEnter: function(args)
    {
        console.log("[+] SpendGems Hook onEnter()");
        console.log("    args[0] : " + args[0]);
        console.log("    args[1] : " + args[1]);
    },
    onLeave: function(retVal)
    {
        console.log("    retVal : " + retVal);
        console.log("");
    }
});



// public void OnRewardOpened() { } // RVA: 0x541A14 Offset: 0x541A14

var offset = 0x541A14;
var OnRewardOpened = il2cpp.add(offset);

Interceptor.attach(OnRewardOpened,
{
    onEnter: function(args)
    {
        console.log("[+] OnRewardOpened Hook onEnter()");
        console.log("    args[0] : " + args[0]);
    },
    onLeave: function(retVal)
    {
        console.log("");
    }
});



// public void OnRewardx3() { } // RVA: 0x541BD4 Offset: 0x541BD4

var offset = 0x541BD4;
var OnRewardx3 = il2cpp.add(offset);

Interceptor.attach(OnRewardx3,
{
    onEnter: function(args)
    {
        console.log("[+] OnRewardx3 Hook onEnter()");
        console.log("    args[0] : " + args[0]);
    },
    onLeave: function(retVal)
    {
        console.log("");
    }
});



// public void SetDDReward() { } // RVA: 0x541D00 Offset: 0x541D00

var offset = 0x541D00;
var SetDDReward = il2cpp.add(offset);

Interceptor.attach(SetDDReward,
{
    onEnter: function(args)
    {
        console.log("[+] SetDDReward Hook onEnter()");
        console.log("    args[0] : " + args[0]);
    },
    onLeave: function(retVal)
    {
        console.log("");
    }
});
  
  
  
  
