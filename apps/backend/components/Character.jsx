import CharacterLeftColumn from "../../frontend/ZZZOptimizer/src/components/CharacterPage/CharacterLeftColumn";

export default function Character(){
	let CharacterInfo = [
		{
			"characterName": "Rina (Alexandrina Sebastiane)",
			"rank": "S",
			"attribute": "Electric",
			"style": "Support",
			"faction": "Victoria Housekeeping",
			"type": "Strike",
			"icon": require("../../assets/logo/agents/Rina.jpg")
		},
		{
			"characterName": "Anby Demara",
			"rank": "A",
			"attribute": "Electric",
			"style": "Stun",
			"faction": "Cunning Hares",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Anby.jpg")
		},
		{
			"characterName": "Anton Ivanov",
			"rank": "A",
			"attribute": "Electric",
			"style": "Attack",
			"faction": "Belobog Heavy Industries",
			"type": "Pierce",
			"icon": require("../../assets/logo/agents/Anton.jpg")
		},
		{
			"characterName": "Ben Bigger",
			"rank": "A",
			"attribute": "Fire",
			"style": "Defense",
			"faction": "Belobog Heavy Industries",
			"type": "Strike",
			"icon": require("../../assets/logo/agents/Ben.jpg")
		},
		{
			"characterName": "Billy Kid",
			"rank": "A",
			"attribute": "Physical",
			"style": "Attack",
			"faction": "Cunning Hares",
			"type": "Pierce",
			"icon": require("../../assets/logo/agents/Billy.jpg")
		},
		{
			"characterName": "Corin Wickes",
			"rank": "A",
			"attribute": "Physical",
			"style": "Attack",
			"faction": "Victoria Housekeeping",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Corin.jpg")
		},
		{
			"characterName": "Ellen Joe",
			"rank": "S",
			"attribute": "Ice",
			"style": "Attack",
			"faction": "Victoria Housekeeping",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Ellen.jpg")
		},
		{
			"characterName": "Koleda Belobog",
			"rank": "S",
			"attribute": "Fire",
			"style": "Stun",
			"faction": "Belobog Heavy Industries",
			"type": "Strike",
			"icon": require("../../assets/logo/agents/Koleda.jpg")
		},
		{
			"characterName": "Lucy (Luciana de Montefio)",
			"rank": "A",
			"attribute": "Fire",
			"style": "Support",
			"faction": "Sons of Calydon",
			"type": "Strike",
			"icon": require("../../assets/logo/agents/Lucy.jpg")
		},
		{
			"characterName": "Nekomata (Nekomiya Mana)",
			"rank": "S",
			"attribute": "Physical",
			"style": "Attack",
			"faction": "Cunning Hares",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Nekomata.jpg")
		},
		{
			"characterName": "Nicole Demara",
			"rank": "A",
			"attribute": "Ether",
			"style": "Support",
			"faction": "Cunning Hares",
			"type": "Strike",
			"icon": require("../../assets/logo/agents/Nicole.jpg")
		},
		{
			"characterName": "Piper Wheel",
			"rank": "A",
			"attribute": "Physical",
			"style": "Anomaly",
			"faction": "Sons of Calydon",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Piper.jpg")
		},
		{
			"characterName": "Soldier11",
			"rank": "S",
			"attribute": "Fire",
			"style": "Attack",
			"faction": "Obol Squad",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Soldier11.jpg")
		},
		{
			"characterName": "Soukaku",
			"rank": "A",
			"attribute": "Ice",
			"style": "Support",
			"faction": "Section 6",
			"type": "Slash",
			"icon": require("../../assets/logo/agents/Soukaku.jpg")
		},
		{
			"characterName": "Von Lycaon",
			"rank": "S",
			"attribute": "Ice",
			"style": "Stun",
			"faction": "Victoria Housekeeping",
			"type": "Strike",
			"icon": require("../../assets/logo/agents/Lycaon.jpg")
		},
		{
			"characterName": "Zhu Yuan",
			"rank": "S",
			"attribute": "Ether",
			"style": "Attack",
			"faction": "Criminal Investigation Special Response Team",
			"type": "Pierce",
			"icon": require("../../assets/logo/agents/Yuan.jpg")
		}
	]

	return <div>
		<CharacterLeftColumn list={CharacterInfo}>
			
		</CharacterLeftColumn>
	</div>
}
