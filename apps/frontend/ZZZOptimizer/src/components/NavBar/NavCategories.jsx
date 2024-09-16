import React from "react";
import "./nav.css";
import util from "../../util";

function NavCategories() {
  return (
    <div className="nav-item categories-holder">
      <ul className="categories">
        {/* Agent  */}
        <li className="nav-item">
          <a href="/deploy-github/agents" className="nav-link collapsed">
            <img
              alt="agent Icon"
              src={util.navIcon.agent}
              className="nav-icon"
            ></img>
            <span>Agents</span>
          </a>
        </li>

        {/* W-Engine */}
        <li className="nav-item">
          <a href="/deploy-github/w-engine" className="nav-link collapsed">
            <img
              alt="W-Engine Icon"
              src={util.navIcon.wEngine}
              className="nav-icon"
            />
            <span>W-Engines</span>
          </a>
        </li>

        {/* Drive Disc */}
        <li className="nav-item">
          <a href="/deploy-github/drive-disk" className="nav-link collapsed">
            <img alt="Icon" src={util.navIcon.driveDisc} className="nav-icon" />
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
            <img
              alt="bangbooIcon"
              src={util.navIcon.bangboo}
              className="nav-icon"
            />
            <span>Bangboo</span>
          </a>
        </li>
      </ul>
    </div>
  );
}

export default NavCategories;
