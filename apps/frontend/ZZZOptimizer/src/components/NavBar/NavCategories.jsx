import React from "react";
import "./nav.css";
import engineIcon from "../../assets/icon/wEngine/W-Engine.jpg";
import discIcon from "../../assets/icon/driveDisc/Drive-Disc.jpg";
import bangbooIcon from "../../assets/icon/bangboos/Bangboo.jpg";
import agentIcon from "../../assets/icon/agents/agents.jpg";

function NavCategories() {
  return (
    <div className="nav-item categories-holder">
      <ul className="categories">
        {/* Agent  */}
        <li className="nav-item">
          <a href="/deploy-github/agents" className="nav-link collapsed">
            <img alt="agent Icon" src={agentIcon} className="nav-icon"></img>
            <span>Agents</span>
          </a>
        </li>

        {/* W-Engine */}
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <img alt="W-Engin Icon" src={engineIcon} className="nav-icon" />
            <span>W-Engines</span>
          </a>
        </li>

        {/* Drive Disc */}
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <img alt="Icon" src={discIcon} className="nav-icon" />
            <span>Drive-Discs</span>
          </a>
        </li>

        {/* Team Comps */}
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <i className="bi bi-people"></i>
            <span>Team Comps</span>
          </a>
        </li>

        {/* Bangboos */}
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <img alt="bangbooIcon" src={bangbooIcon} className="nav-icon" />
            <span>Bangboo</span>
          </a>
        </li>
      </ul>
    </div>
  );
}

export default NavCategories;
