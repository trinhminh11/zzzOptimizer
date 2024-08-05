import React from "react";
import fireLogo from "../../assets/logo/agentsAttributes/Icon_Fire.jpg";
import electricLogo from "../../assets/logo/agentsAttributes/Icon_Electric.jpg";
import etherLogo from "../../assets/logo/agentsAttributes/Icon_Ether.jpg";
import iceLogo from "../../assets/logo/agentsAttributes/Icon_Ice.jpg";
import physicalLogo from "../../assets/logo/agentsAttributes/Icon_Physical.jpg";
import "./character.css";
// import demoData from "../../../../../backend/components/character.json";
// import demoData from "./demo.json";

function CharacterLeftColumn({ list }) {
  return (
    <div className="row left-table">
      {/* Search Bar  */}
      <div className="search-bar">
        <input type="text" placeholder="Search a champion"></input>
      </div>

      {/* Filter Bar  */}
      <div className="filter-bar">
        {/* Elements */}
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

      {/* Champion display */}
      <div className="champion-grid">
        {/* {demoData.map((demoData) => {
          const location = demoData.img;
          return (
            <div className="champion" key={`${demoData.characterName}`}>
              {console.log(demoData.img)}
              <img src={require(location)} alt="demo"></img>
              <div className="name-showcase">{demoData.characterName} </div>
            </div>
          );
        })} */}

        {list.map((value) => {
          console.log(value);
          return (
            <div className="champion" key={`${value.characterName}`}>
              {/* {console.log(CharacterInfo.img)} */}
              <img src={require(value.icon)} alt="demo"></img>
              <div className="name-showcase">{value.characterName} </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default CharacterLeftColumn;
