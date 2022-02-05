## Overview

In this article we make a value proposition for Algorand Ecosystem to consider benefits of Machine Learning coupled with an Indexer.

First, we build an interface to Algorand with AlgoSigner Wallet in React

Next, we connect an Indexer to our application by using testnet API from PureStake. 

Finally, we provide a roadmap to extend the application to an ML model with the combination of smart contracts to implement a version of a on-chain exchange.

### Algorand Layer 1 Capabilities

One of the greatest benefits of building a project on Algorand are its Layer 1 capabilities and payment patterns.

The Algorand protocol supports the creation of on-chain assets that benefit from the same security, compatibility, speed and ease of use as the Algo. The official name for assets on Algorand is Algorand Standard Assets (ASA).

Developers and organizations can represent stablecoins, loyalty points, system credits, and in-game points with Algorand Standard Assets.
Meanhwhile an optional functionality to place transfer restrictions on an asset helps support more complex use cases such as securities, compliance, and certification.

Algorand enables bundling of transactions in [atomic swaps](https://developer.algorand.org/docs/get-details/atomic_transfers/) where each transaction relies on each other. 
Which is particularly important since it emphasises security and low transaction costs.

Besides, another Layer 1 capability is [smart signatures](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/#smart-signatures) that are used for signature delegation. This feature significantly raises the bar for the control of an escrow account, a third-party smart contract which holds tokens until the payment conditions are satisfied.

We can build smart contracts on Algorand using Python and [PyTeal](https://github.com/algorand/pyteal) Library. Here is the Github repository that walkthoughs the creation of your first Algorand accounts, creation and distribute your first asset or token on the Algorand blockchain, trading your token "atomically" without any third party and obtaining 
asset with the help of smart signature (stateless smart contract).

Finally, we can search the Algorand Blockchain using the [Indexer](https://developer.algorand.org/docs/get-details/indexer/).
The Indexer provides a set of REST API calls for searching blockchain Transactions, Accounts, Assets and Blocks with refined searches. 

![image](https://user-images.githubusercontent.com/66903336/152649700-cde7103e-d2c6-4026-bc86-98e3d7c01d22.png)

The latest Algorand native SDKs (Python, JavaScript, Go, and Java) provide similar functionality. These REST calls are based on the Open API specification and are described in the REST SDK reference documentation. 
[Developer Office Hours on Algorand Indexer](https://www.youtube.com/watch?v=m8gooZ_VDeY) provides practical overview for the developers.

## Big Data and Analytics

The Business Process Management (BPM) is the science and practice of overseeing work to ensure consistent outcomes and to leverage opportunities for process improvement. BPM activities are commonly organized along lifecycle phases: identification, discovery, analysis, improvement, implementation, monitoring, and controlling.

Data-driven approach to analysis, monitoring, and controlling phases assist in aalysis and monitoring of running processes. Organization leaders and key members can determine how well they are performing on core objectives and performance metrics. Furthermore, collected data and estimations serve as vital inputs for community architecture and pipelines during the redesign phase.

Data-driven approaches make use of data not only for process discovery or analysis, but also in monitoring to gain predictive insights.
Data utilisation has moved from only offline mode, to runtime phases such as monitoring, where data is used in real-time to forecast process behavior, performance, and outcomes.
In general, process outcomes reflect the quality of a result delivered to actors involved in a process.

Predictive process monitoring at runtime is especially growing in importance. Predicting the remaining cycle time, compliance, sequence of process activities, the final or partial outcome, or the prioritization of processes helps organizations to make decisions and gain valuable insights in a rapidly evolving environment.

A convergence of breakthrough technologies in big data and data analytics provide a critical solution to meet organization objectives. Big data and advanced analytics play a key role in raising productivity of knowledge-intensive tasks, maximizing assets, and facilitating personalized digital experience.

## React

We have chosen React as our front end JavaScript Library. In fact, according to [Stack Overflow developer annual survey](https://developer-tech.com/news/2021/aug/03/2021-stack-overflow-survey-react-js-takes-the-web-framework-crown-python-is-in-demand-and-devs-still-love-rust/), React.js (40.14%) has overtaken jQuery (34.42%) to become the most-used web framework. Besides, React.js (25.12%) also leads the most-wanted web frameworks, followed by Vue.js (16.69%), Django (9.21%), Angular (8.47%), and Svelte (6.57%). 

First we are creating the react app by using npx, npm package runner:
`npx create-react-app new-app`
and move into the directory folder
`cd new-app`
To work with algorand we need algosdk dependency and to make our life easier with html elements later we also install [semantic-ui-react](https://semantic-ui.com/).
`npm i algosdk semantic-ui-react`

### First Step: implementing AlgoSigner Wallet

Currently we are working in App.js, where we are implementing a connection to [AlgoSigner](https://github.com/PureStake/algosigner):


```javascript
/* global AlgoSigner */
import './App.css';
import {Button, Container, Header, Message} from "semantic-ui-react";
import {useState, useCallback} from "react";

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

const App = () => {
  return (
    <Container className="App">
      
      <Header as="h1" dividing>React App Using AlgoSigner</Header>

      <CheckAlgoSigner/>

      <GetAccounts/>

    </Container>
  );
};

export default App;
```

### Second Step: connecting to the Indexer

To connect to the testnet we are using purestake.io API to access the indexer. We add following lines in our file as well as a function to get the timestamp of the block :


```javascript
import algosdk from 'algosdk';

const baseServer = "https://testnet-algorand.api.purestake.io/idx2";
const port = "";
const token = {
  'X-API-key': 'API-code-should-be-in-this-place',
}

let indexerClient = new algosdk.Indexer(token, baseServer, port);
```


```javascript
const GetBlocks = () => {
  const action = useCallback(async () => {

    let blockInfo = await indexerClient.lookupBlock(5).do()
    return blockInfo['timestamp']

}, []);

  return <ExampleAlgoSigner title="Get Blocks" buttonText="Get B" buttonAction={action}/>
};
```

Combined the code the file loos as following:

```javascript
/* global AlgoSigner */
import './App.css';
import {Button, Container, Header, Message} from "semantic-ui-react";
import {useState, useCallback} from "react";
import algosdk from 'algosdk';

const baseServer = "https://testnet-algorand.api.purestake.io/idx2";
const port = "";
const token = {
  'X-API-key': '',
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
```

### Roadmap

We consider to process and store Algorand Blockchain data in PostgreSQL, for instance, to assess the credibility of the users.
![image](https://user-images.githubusercontent.com/66903336/152650816-53ea89b4-b8f3-4012-9da0-be851256726f.png)

For instance, we could use the transaction and balance history to implement the trust score.

Next, we collect the data that is clean and regularized, designed to be usable right away to train the models.

Besides, we intend tio host a machine learning model using React and Flask. However, we have not decided yet whtehr it is more beneficia to train and host an machine learning model directly in React by using [tensorflow.js](https://www.tensorflow.org/js).

Ideally, as the final product this model would connect to an indexer data in real time and feed the data to an algorithm that would estimate the probability of an event such as sale and predict the future price movements of an asset. 
