import React from "react";
import WEngineLocalDatabase from "./WEngineLocalDatabase";
import WEngineDatabase from "./WEngineDatabase";
import "./wEngine.css";
import { useState, useEffect } from "react";
import { WEngineService } from "../../services/WEngineService";

function WEngineBody({ selectedOptions, setSelectedOptions }) {
  // set up list for storing wEngine from api
  const [listWEngines, setListWEngines] = useState([]);

  //set up local storage for storing information
  const [listSelectedWEngines, setListSelectedWEngines] = useState(() => {
    //Check local storage and initialize list
    const storedWEngines = localStorage.getItem("selected wEngine");
    return storedWEngines ? JSON.parse(storedWEngines) : [];
  });

  // Set up function for storing data from api into the list
  useEffect(() => {
    getWEngines();
  }, []);

  const getWEngines = async () => {
    let res = await WEngineService();
    if (res) {
      setListWEngines(res);
    }
  };

  return (
    <div className="row wEngine-body">
      <div className="col-lg-3">
        <WEngineDatabase
          listWEngines={listWEngines}
          listSelectedWEngines={listSelectedWEngines}
          setListSelectedWEngines={setListSelectedWEngines}
          selectedOptions={selectedOptions}
          setSelectedOptions={setSelectedOptions}
        />
      </div>
      <div className="col-lg-9">
        <WEngineLocalDatabase
          listSelectedWEngines={listSelectedWEngines}
          setListSelectedWEngines={setListSelectedWEngines}
          selectedOptions={selectedOptions}
          setSelectedOptions={setSelectedOptions}
        />
      </div>
    </div>
  );
}

export default WEngineBody;
