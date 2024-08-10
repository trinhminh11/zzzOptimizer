import React from "react";
import "./agent.css";
import fireIcon from "../../assets/icon/agentsAttributes/Icon_Fire.jpg";
import electricIcon from "../../assets/icon/agentsAttributes/Icon_Electric.jpg";
import etherIcon from "../../assets/icon/agentsAttributes/Icon_Ether.jpg";
import iceIcon from "../../assets/icon/agentsAttributes/Icon_Ice.jpg";
import physicalIcon from "../../assets/icon/agentsAttributes/Icon_Physical.jpg";
import sRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_S.jpg";
import aRankIcon from "../../assets/icon/agentsRanks/Icon_AgentRank_A.jpg";
import attackIcon from "../../assets/icon/agentsRoles/Icon_Attack.jpg";
import anomalyIcon from "../../assets/icon/agentsRoles/Icon_Anomaly.jpg";
import defenseIcon from "../../assets/icon/agentsRoles/Icon_Defense.jpg";
import stunIcon from "../../assets/icon/agentsRoles/Icon_Stun.jpg";
import supportIcon from "../../assets/icon/agentsRoles/Icon_Support.jpg";

export default function AgentSort() {
  return (
    <div className=" agent-sorting-container">
      {/* Rank  */}
      <div className="sorting-categories rank-sort">
        <div className="element-sort">
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a className="element-sort">
          <img alt="S rank Icon" src={sRankIcon} className="nav-icon" />
        </a>

        <a className="element-sort">
          <img alt="A rank Icon" src={aRankIcon} className="nav-icon" />
        </a>
      </div>

      {/* Element */}

      <div className="sorting-categories attribute-sort">
        <div className="element-sort">
          <i class="bi bi-asterisk select-all"></i>
        </div>

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

      {/* Fighting Style */}
      <div className="sorting-categories fighting-sort">
        <div className="element-sort">
          <i class="bi bi-asterisk select-all"></i>
        </div>

        <a className="element-sort">
          <img alt="Attack Icon" src={attackIcon} className="nav-icon" />
        </a>

        <a className="element-sort">
          <img alt="Anomaly Icon" src={anomalyIcon} className="nav-icon" />
        </a>

        <a className="element-sort">
          <img alt="Defense Icon" src={defenseIcon} className="nav-icon" />
        </a>

        <a className="element-sort">
          <img alt="Stun Icon" src={stunIcon} className="nav-icon" />
        </a>

        <a className="element-sort">
          <img alt="Support Icon" src={supportIcon} className="nav-icon" />
        </a>
      </div>
    </div>
  );
}
