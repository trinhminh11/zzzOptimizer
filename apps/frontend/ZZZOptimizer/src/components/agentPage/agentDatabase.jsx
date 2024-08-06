import React from "react";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import "./agent.css";
// import demoData from "../../../../../backend/components/character.json";
// import demoData from "./demo.json";

function agentDatabase({ agentInfoList }) {
  return (
    <div className="row left-table">
      {/* Search Bar  */}
      <div className="search-bar">
        <input type="text" placeholder="Search an agent"></input>
      </div>

      {/* Filter Bar  */}
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

      {/* Champion display */}
      <div className="agent-grid">
        {agentInfoList.map((agent) => {
          return (
            <div className="agent" key={`${agent.characterName}`}>
              <img src={agent.icon} alt="demo"></img>
              <div className="agent-name-showcase">{agent.characterName} </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default agentDatabase;
