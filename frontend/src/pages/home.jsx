/* global AlgoSigner */
import { useState, useCallback } from "react";
import algosdk from "algosdk";
import { motion } from "framer-motion";
const baseServer = "https://testnet-algorand.api.purestake.io/idx2";
const port = "";
const token = {
  "X-API-key": "B3SU4KcVKi94Jap2VXkK83xx38bsv95K5UZm2lab",
};

let indexerClient = new algosdk.Indexer(token, baseServer, port);

const ExampleAlgoSigner = ({ title, buttonText, buttonAction }) => {
  const [result, setResult] = useState("");

  const onClick = useCallback(async () => {
    const r = await buttonAction();
    setResult(r);
  }, [buttonAction]);

  return (
    <div className="my-4">
      <h2>{title}</h2>
      <motion.button
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        className="bg-blue-500 transition p-2 shadow-lg shadow-blue-500/50 text-white rounded-lg m-1"
        onClick={onClick}
      >
        {buttonText}
      </motion.button>
      {result && (
        <div className="bg-emerald-500 m-2 p-1 text-gray-100 rounded-sm shadow-emerald-500/50">
          <code>{result}</code>
        </div>
      )}
    </div>
  );
};

const CheckAlgoSigner = () => {
  const action = useCallback(() => {
    if (typeof AlgoSigner !== "undefined") {
      return "AlgoSigner is installed.";
    } else {
      return "AlgoSigner is NOT installed.";
    }
  }, []);

  return (
    <ExampleAlgoSigner
      title="CheckAlgoSigner"
      buttonText="Check"
      buttonAction={action}
    />
  );
};

const GetAccounts = () => {
  const action = useCallback(async () => {
    await AlgoSigner.connect({
      ledger: "TestNet",
    });
    const accts = await AlgoSigner.accounts({
      ledger: "TestNet",
    });
    return JSON.stringify(accts, null, 2);
  }, []);

  return (
    <ExampleAlgoSigner
      title="Get Accounts"
      buttonText="Get Accounts"
      buttonAction={action}
    />
  );
};

const GetBlocks = () => {
  const action = useCallback(async () => {
    let blockInfo = await indexerClient.lookupBlock(5).do();
    return blockInfo["timestamp"];
  }, []);

  return (
    <ExampleAlgoSigner
      title="Get Blocks"
      buttonText="Get Block"
      buttonAction={action}
    />
  );
};

const Home = () => {
  return (
      <div className="container mt-4 mx-2">
        <h1 className="text-center">AlgoSigner</h1>
        <CheckAlgoSigner />
        <GetAccounts />
        <GetBlocks />
      </div>
  );
};

export default Home;
