import React from "react";
import "./nav.css";
import engineLogo from "../../assets/logo/wEngine/W-Engine.jpg";
import discLogo from "../../assets/logo/driveDisc/Drive-Disc.jpg";
import bangbooLogo from "../../assets/logo/bangboos/Bangboo.jpg";

function NavCategories() {
  return (
    <div className="nav-item categories-holder">
      <ul className="categories">
        {/* Character  */}
        <li className="nav-item">
          <a href="/deploy-github/characters" className="nav-link collapsed">
            <i className="bi bi-person"></i>
            <span>Agents</span>
          </a>
        </li>

        {/* W-Engine */}
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <img alt="W-Engin Logo" src={engineLogo} className="nav-icon" />
            <span>W-Engine</span>
          </a>
        </li>

        {/* Drive Disc */}
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <img alt="Logo" src={discLogo} className="nav-icon" />
            <span>Drive-Disc</span>
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
            <img alt="bangbooLogo" src={bangbooLogo} className="nav-icon" />
            <span>Bangboo</span>
          </a>
        </li>
      </ul>
    </div>
  );
}

export default NavCategories;
