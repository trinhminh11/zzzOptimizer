import React from "react";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import "./agent.css";
import attackIcon from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import anomalyIcon from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import defenseIcon from "../../assets/icon/agentsRoles/Icon_Defense.jpg";
import stunIcon from "../../assets/icon/agentsRoles/Icon_Stun.jpg";
import supportIcon from "../../assets/icon/agentsRoles/Icon_Support.jpg";
import { useState, useEffect } from "react";

function AgentDatabase({ agentInfoList }) {
  const handleAgentClick = (agent) => {
    localStorage.setItem("selectedAgent", JSON.stringify(agent));
    console.log(`${agent.characterName} clicked`);
  };

  return (
    <div className="row left-table">
      {/* Search Bar  */}
      <div className="search-bar">
        <input type="text" placeholder="Search an agent"></input>
      </div>

      {/* Attribute Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
        <button type="button" className="btn btn-secondary">
          <img alt="Electric Icon" src={electricIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Fire Icon" src={fireIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Physical Icon" src={physicalIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Ice Icon" src={iceIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Ether Icon" src={etherIcon} className="nav-icon" />
        </button>
      </div>

      {/* Fighting style Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
        <button type="button" className="btn btn-secondary">
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </button>
      </div>

      {/* Champion display */}
      <div className="agent-grid">
        {agentInfoList.map((agent) => {
          return (
            <div
              className="agent"
              key={agent.characterName}
              onClick={() => handleAgentClick(agent)}
            >
              <img src={agent.icon} alt="demo"></img>
              <div className="agent-name-showcase">{agent.characterName} </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default AgentDatabase;
