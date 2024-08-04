import React from "react";
import "./nav.css";

function NavCategories() {
  return (
    <div className="nav-item categories-holder">
      <ul className="categories">
        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <i className="bi bi-person"></i>
            <span>Characters</span>
          </a>
        </li>

        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <i className="bi bi-people"></i>
            <span>Team Comps</span>
          </a>
        </li>

        <li className="nav-item">
          <a href="#" className="nav-link collapsed">
            <i className="bi bi-people"></i>
            <span>W-Engine</span>
          </a>
        </li>
      </ul>
    </div>
  );
}

export default NavCategories;
