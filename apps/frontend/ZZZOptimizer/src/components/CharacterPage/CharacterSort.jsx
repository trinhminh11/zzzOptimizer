import React from "react";
import "./character.css";
import fireLogo from "../../assets/logo/Icon_Fire.jpg";
import electricLogo from "../../assets/logo/Icon_Electric.jpg";
import etherLogo from "../../assets/logo/Icon_Ether.jpg";
import iceLogo from "../../assets/logo/Icon_Ice.jpg";
import physicalLogo from "../../assets/logo/Icon_Physical.jpg";

function CharacterSort() {
  return (
    <div className="row character-sorting-container">
      <button type="button" className="btn btn-secondary">
        <span>Version: demo</span>
      </button>
      <button type="button" className="btn btn-secondary">
        <img alt="Electric Logo" src={electricLogo} className="nav-icon" />
        <span>Electric</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Fire Logo" src={fireLogo} className="nav-icon" />
        <span>Fire</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Physical Logo" src={physicalLogo} className="nav-icon" />
        <span>Physical</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Ice Logo" src={iceLogo} className="nav-icon" />
        <span>Ice</span>
      </button>

      <button type="button" className="btn btn-secondary">
        <img alt="Ether Logo" src={etherLogo} className="nav-icon" />
        <span>Ether</span>
      </button>
    </div>
  );
}

export default CharacterSort;
