import React from "react";
import fireLogo from "../../assets/logo/Icon_Fire.jpg";
import electricLogo from "../../assets/logo/Icon_Electric.jpg";
import etherLogo from "../../assets/logo/Icon_Ether.jpg";
import iceLogo from "../../assets/logo/Icon_Ice.jpg";
import physicalLogo from "../../assets/logo/Icon_Physical.jpg";
import agentRinaLogo from "../../assets/logo/agents/Agent_Rina_Icon.jpg";
import "./character.css";

function CharacterLeftColumn() {
  return (
    <div className="row left-table">
      <div className="search-bar">
        <input type="text" placeholder="Search a champion"></input>
      </div>

      <div class="filter-bar">
        <button type="button" className="btn btn-secondary">
          <img alt="Electric Logo" src={electricLogo} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Fire Logo" src={fireLogo} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Physical Logo" src={physicalLogo} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Ice Logo" src={iceLogo} className="nav-icon" />
        </button>

        <button type="button" className="btn btn-secondary">
          <img alt="Ether Logo" src={etherLogo} className="nav-icon" />
        </button>
      </div>

      <div className="champion-grid">
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name"> Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
        <div className="champion">
          <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
          <span className="champion-name">Alexandrina Sebastiane</span>
        </div>
      </div>
    </div>
  );
}

export default CharacterLeftColumn;
