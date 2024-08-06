import React from "react";
import "./agent.css";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";

function agentSort() {
  return (
    <div className="row agent-sorting-container">
      <button type="button" className="btn btn-secondary">
        <span>Version: demo</span>
      </button>
      <button type="button" className="btn btn-secondary">
        <img alt="Electric Icon" src={electricIcon} className="nav-icon" />
        <span>Electric</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Fire Icon" src={fireIcon} className="nav-icon" />
        <span>Fire</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Physical Icon" src={physicalIcon} className="nav-icon" />
        <span>Physical</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Ice Icon" src={iceIcon} className="nav-icon" />
        <span>Ice</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Ether Icon" src={etherIcon} className="nav-icon" />
        <span>Ether</span>
      </button>
    </div>
  );
}

export default agentSort;
