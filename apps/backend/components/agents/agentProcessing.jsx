import AgentInfo from "./agentInfo"
import agentBaseStat from "./agentBaseStat.json"

import React from 'react';

class Agent {
	name
    level
    promotion
    attribute
    fightingStyle
    type

    hp
    hp_
    atk
    atk_
    def
    def_
    impact
    critRate_
    critDmg_
    anoMas
    anoPro
    pen
    pen_
    enerGen
    electricDMG_
    physicalDMG_
    fierDMG_
    iceDMG_
    etherDMG_

    constructor(name, level, promotion, attribute, fightingStyle, type){
        this.name = name;
        this.promotion = promotion;
        this.level = level;
        this.attribute = attribute;
        this.fightingStyle = fightingStyle;
        this.type = type;
    }

    loadBaseStat(data){
        this.baseStat = data;
    }

    set setLevel(value){
        this.level = value;
        this.calculationStat();
    }

    calculationStat(){
    }
}

class Ellen extends Agent {
    baseStat
    constructor(){
        super("Ellen Joe", 1, 0, "Ice", "Attack", "Slash");
        this.calculationStat();
    }
    

    calculationStat(){
    }
}

class AgentProcessing extends React.Component{
    agents = ["Hello"];
    render() {
        return (
          <div/>
        );
      }
}

export default AgentProcessing;
