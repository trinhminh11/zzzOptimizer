import React from "react";
import "./agent.css";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import sRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_S.jpg";
import aRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_A.jpg";

export default function AgentSort() {
  return (
    <div className="row agent-sorting-container">
      <button type="button" className="btn btn-secondary">
        <span>Version: demo</span>
      </button>

      {/* Rank  */}
      <a className="element-sort">
        <img alt="S rank Icon" src={sRankIcon} className="nav-icon" />
      </a>

      <a className="element-sort">
        <img alt="A rank Icon" src={aRankIcon} className="nav-icon" />
      </a>

      {/* Element */}
      <a className="element-sort">
        <img alt="Electric Icon" src={electricIcon} className="nav-icon" />
      </a>

      <a className="element-sort">
        <img alt="Fire Icon" src={fireIcon} className="nav-icon" />
      </a>

      <a className="element-sort">
        <img alt="Physical Icon" src={physicalIcon} className="nav-icon" />
      </a>

      <a className="element-sort">
        <img alt="Ice Icon" src={iceIcon} className="nav-icon" />
      </a>

      <a className="element-sort">
        <img alt="Ether Icon" src={etherIcon} className="nav-icon" />
      </a>
    </div>
  );
}
