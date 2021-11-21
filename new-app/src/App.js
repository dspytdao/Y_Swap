/* global AlgoSigner */
import './App.css';
import {Button, Container, Header, Message} from "semantic-ui-react";
import {useState, useCallback} from "react";
import algosdk from 'algosdk';

const baseServer = "https://testnet-algorand.api.purestake.io/idx2";
const port = "";
const token = {
  'X-API-key': 'B3SU4KcVKi94Jap2VXkK83xx38bsv95K5UZm2lab',
}

let indexerClient = new algosdk.Indexer(token, baseServer, port);

const ExampleAlgoSigner = ({title, buttonText, buttonAction}) => {
  const [result, setResult] = useState("");

  const onClick = useCallback(async () => {
    const r = await buttonAction();
    setResult(r);
  }, [buttonAction]);

  return (
    <>
      <Header as="h2" dividing>{title}</Header>
      <Button primary={true} onClick={onClick}>{buttonText}</Button>
      <Message>
        <code>
          {result}
        </code>
      </Message>
    </>
  );
};

const CheckAlgoSigner = () => {
  const action = useCallback(() => {
    if (typeof AlgoSigner !== 'undefined') {
      return "AlgoSigner is installed.";
    } else {
      return "AlgoSigner is NOT installed.";
    }
  }, []);

  return <ExampleAlgoSigner title="CheckAlgoSigner" buttonText="Check" buttonAction={action}/>
};

const GetAccounts = () => {
  const action = useCallback(async () => {
    await AlgoSigner.connect({
      ledger: 'TestNet'
    });
    const accts = await AlgoSigner.accounts({
      ledger: 'TestNet'
    });
    return JSON.stringify(accts, null, 2);
  }, []);

  return <ExampleAlgoSigner title="Get Accounts" buttonText="Get Accounts" buttonAction={action}/>
};

const GetBlocks = () => {
  const action = useCallback(async () => {

    let blockInfo = await indexerClient.lookupBlock(5).do()
    return blockInfo['timestamp']

}, []);

  return <ExampleAlgoSigner title="Get Blocks" buttonText="Get B" buttonAction={action}/>
};

const App = () => {
  return (
    <Container className="App">
      
      <Header as="h1" dividing>React App Using AlgoSigner</Header>

      <CheckAlgoSigner/>

      <GetAccounts/>

      <GetBlocks/>

    </Container>
  );
};

export default App;
