import AgentDatabase from "../../frontend/ZZZOptimizer/src/components/agentPage/agentDatabase";


export default function agentInfo({agents}) {
  let agentIconFolder = "../../frontend/ZZZOptimizer/src/assets/icon/agents/";
  
  const agentsJson = [
    {
      characterName: "Rina (Alexandrina Sebastiane)",
      rank: "S",
      attribute: "Electric",
      style: "Support",
      faction: "Victoria Housekeeping",
      type: "Strike",
      icon: require(agentIconFolder + "Rina.jpg"),
    },
    {
      characterName: "Anby Demara",
      rank: "A",
      attribute: "Electric",
      style: "Stun",
      faction: "Cunning Hares",
      type: "Slash",
      icon: require(agentIconFolder + "Anby.jpg"),
    },
    {
      characterName: "Anton Ivanov",
      rank: "A",
      attribute: "Electric",
      style: "Attack",
      faction: "Belobog Heavy Industries",
      type: "Pierce",
      icon: require(agentIconFolder + "Anton.jpg"),
    },
    {
      characterName: "Ben Bigger",
      rank: "A",
      attribute: "Fire",
      style: "Defense",
      faction: "Belobog Heavy Industries",
      type: "Strike",
      icon: require(agentIconFolder + "Ben.jpg"),
    },
    {
      characterName: "Billy Kid",
      rank: "A",
      attribute: "Physical",
      style: "Attack",
      faction: "Cunning Hares",
      type: "Pierce",
      icon: require(agentIconFolder + "Billy.jpg"),
    },
    {
      characterName: "Corin Wickes",
      rank: "A",
      attribute: "Physical",
      style: "Attack",
      faction: "Victoria Housekeeping",
      type: "Slash",
      icon: require(agentIconFolder + "Corin.jpg"),
    },
    {
      characterName: "Ellen Joe",
      rank: "S",
      attribute: "Ice",
      style: "Attack",
      faction: "Victoria Housekeeping",
      type: "Slash",
      icon: require(agentIconFolder + "Ellen.jpg"),
    },
    {
      characterName: "Koleda Belobog",
      rank: "S",
      attribute: "Fire",
      style: "Stun",
      faction: "Belobog Heavy Industries",
      type: "Strike",
      icon: require(agentIconFolder + "Koleda.jpg"),
    },
    {
      characterName: "Lucy (Luciana de Montefio)",
      rank: "A",
      attribute: "Fire",
      style: "Support",
      faction: "Sons of Calydon",
      type: "Strike",
      icon: require(agentIconFolder + "Lucy.jpg"),
    },
    {
      characterName: "Nekomata (Nekomiya Mana)",
      rank: "S",
      attribute: "Physical",
      style: "Attack",
      faction: "Cunning Hares",
      type: "Slash",
      icon: require(agentIconFolder + "Nekomata.jpg"),
    },
    {
      characterName: "Nicole Demara",
      rank: "A",
      attribute: "Ether",
      style: "Support",
      faction: "Cunning Hares",
      type: "Strike",
      icon: require(agentIconFolder + "Nicole.jpg"),
    },
    {
      characterName: "Piper Wheel",
      rank: "A",
      attribute: "Physical",
      style: "Anomaly",
      faction: "Sons of Calydon",
      type: "Slash",
      icon: require(agentIconFolder + "Piper.jpg"),
    },
    {
      characterName: "Soldier11",
      rank: "S",
      attribute: "Fire",
      style: "Attack",
      faction: "Obol Squad",
      type: "Slash",
      icon: require(agentIconFolder + "Soldier11.jpg"),
    },
    {
      characterName: "Soukaku",
      rank: "A",
      attribute: "Ice",
      style: "Support",
      faction: "Section 6",
      type: "Slash",
      icon: require(agentIconFolder + "Soukaku.jpg"),
    },
    {
      characterName: "Von Lycaon",
      rank: "S",
      attribute: "Ice",
      style: "Stun",
      faction: "Victoria Housekeeping",
      type: "Strike",
      icon: require(agentIconFolder + "Lycaon.jpg"),
    },
    {
      characterName: "Zhu Yuan",
      rank: "S",
      attribute: "Ether",
      style: "Attack",
      faction: "Criminal Investigation Special Response Team",
      type: "Pierce",
      icon: require(agentIconFolder + "Yuan.jpg"),
    },
  ];

  return (
    <div>
      <AgentDatabase agentInfoList={agentsJson} />
    </div>
  );
}

