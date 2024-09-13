function trim(str, ch) {
	var start = 0, 
		end = str.length;
  
	while(start < end && str[start] === ch)
		++start;
  
	while(end > start && str[end - 1] === ch)
		--end;
  
	return (start > 0 || end < str.length) ? str.substring(start, end) : str;
}

let api_dir = "http://127.0.0.1:8000/"
let media_dir = api_dir + "media/"

let util = {
	api_dir: api_dir,
	"trim": trim,
	agentRankIcon: {
		S: media_dir + "agent/rank/S.png",
		A: media_dir + "agent/rank/A.png",
	},
	wEngineRankIcon: {
		S: media_dir + "wengine/rank/S.png",
		A: media_dir + "wengine/rank/A.png",
		B: media_dir + "wengine/rank/B.png" 
	},
	attributeIcon: {
		electric: media_dir + "attribute/Electric.png",
		fire: media_dir + "attribute/Fire.png",
		physical: media_dir + "attribute/Physical.png",
		ice: media_dir + "attribute/Ice.png",
		ether: media_dir + "attribute/Ether.png",
	},
	specialtyIcon: {
		attack: media_dir + "specialty/Attack.png",
		anomaly: media_dir + "specialty/Anomaly.png",
		defense: media_dir + "specialty/Defense.png",
		stun: media_dir + "specialty/Stun.png",
		support: media_dir + "specialty/Support.png",
	},
	navIcon: {
		agent: media_dir + "agent/Agent.png",
		wEngine: media_dir + "wengine/WEngine.png",
		driveDisc: media_dir + "driveDisc/DriveDisc.png",
		bangboo: media_dir + "bangboo/Bangboo.png"
	}
}

export default util;