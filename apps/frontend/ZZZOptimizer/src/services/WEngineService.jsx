import axios from "./customize_axios";

//Get all WEngines
function WEngineService() {
  return axios.get("/wengines");
}

// Get WEngine stat base on LV
const getWEngineStats = (wengine_name, modification, level) => {
  return axios.get(
    `/wengine-stat/${wengine_name}?modification=${modification}&level=${level}`
  );
};

// Get WEngine Description base on Upgrade
const getWEngineDescription = (wengine_name, upgrade) => {
  return axios.get(`/wengine-passive/${wengine_name}?upgrade=${upgrade}`);
};

export { WEngineService, getWEngineStats, getWEngineDescription };
