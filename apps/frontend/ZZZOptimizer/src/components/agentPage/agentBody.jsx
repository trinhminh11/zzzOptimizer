import React from "react";
import "./agent.css";
import AgentLocalDatabase from "./agentLocalDatabase";
import AgentDatabase from "./agentDatabase";
import { AgentsService } from "../../services/AgentService";
import { useState, useEffect } from "react";

function AgentBody({ selectedOptions, setSelectedOptions }) {
  // set up list for storing agent from api
  const [listAgents, setListAgents] = useState([]);

  // set up localstorage for storing infomation
  const [listSelectedAgents, setListSelectedAgents] = useState(() => {
    // Check local storage and initialize list
    const storedAgents = localStorage.getItem("selected agent");
    return storedAgents ? JSON.parse(storedAgents) : [];
  });

  // Set up function to store data from api into the list
  useEffect(() => {
    getAgents();
  }, []);

  const getAgents = async () => {
    let res = await AgentsService();
    if (res) {
      // Add new mindScape attribute
      for (let i = 0; i < res.length; i++) {
        res[i].mindScape = 0;
        res[i].promotion = 0;
        res[i].level = 1;
        res[i].core = 1;
        res[i].basic = 1;
        res[i].dodge = 1;
        res[i].assist = 1;
        res[i].special = 1;
        res[i].chain = 1;
      }
      setListAgents(res);
    }
  };

  return (
    <div className="row agent-body">
      <div className="col-lg-3">
        <AgentDatabase
          listAgents={listAgents}
          listSelectedAgents={listSelectedAgents}
          setListSelectedAgents={setListSelectedAgents}
          selectedOptions={selectedOptions}
          setSelectedOptions={setSelectedOptions}
        />
      </div>
      <div className="col-lg-9">
        <AgentLocalDatabase
          listSelectedAgents={listSelectedAgents}
          setListSelectedAgents={setListSelectedAgents}
          selectedOptions={selectedOptions}
        />
      </div>
    </div>
  );
}

export default AgentBody;
