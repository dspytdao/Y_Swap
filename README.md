## Overview

In this article we build an interface to Algorand with AlgoSigner Wallet.

Make a value proposition for Algroand Ecosystem to consider Machine Learning.

First, we are going to set up a project in React JS and connect AlgoSigner to the Application. 

Next, we connect an Indexer to our application by using testnet API from PureStake. 

Besides, we provide a roadmap to extend the application to an ML model with the combination of smart contracts to implement a version of a on-chain exchange.

### Algorand Layer 1 Capabilities

One of the greatest benefits of building a project on Algorand are its Layer 1 capabilities and payment patterns. 

Algorand enables bundling of transactions in [atomic swaps](https://developer.algorand.org/docs/get-details/atomic_transfers/) where each transaction relies on each other. 
Which is particularly important since it emphasises security and low transaction costs.

Besides, another Layer 1 capability is [smart signatures](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/#smart-signatures) that are used for signature delegation. This feature significantly raises the bar for the control of an escrow account, a third-party smart contract which holds tokens until the payment conditions are satisfied.

Furthermore, we can build smart contracts on Algorand using Python and [PyTeal](https://github.com/algorand/pyteal) Library. Here is the Github repository that walkthoughs the creation of your first Algorand accounts, creation and distribute your first asset or token on the Algorand blockchain, trading your token "atomically" without any third party and obtaining your smartignature (aka stateless smart contract).


## Value Proposition

The Algorand protocol supports the creation of on-chain assets that benefit from the same security, compatibility, speed and ease of use as the Algo. The official name for assets on Algorand is Algorand Standard Assets (ASA).

With Algorand Standard Assets you can represent stablecoins, loyalty points, system credits, and in-game points, just to name a few examples. You can also represent single, unique assets like a deed for a house, collectable items, unique parts on a supply chain, etc. There is also optional functionality to place transfer restrictions on an asset that help support securities, compliance, and certification use cases.

Info

We consider Indexer data to assess the credibility of the issuer.

For instance, we would use the transaction and balance history.

In addition, Liquid and valuable NFTs are a great collateral for options and debt obligations. Machine Learning models have further potential to enhance the precision of the pricing and viability



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


### Further Action

We can host a machine learning model using Python and Flask as written in [this Medium article](https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33). Otherwise, we can train and host an ML model directly in React by using [tensorflow.js](https://dev.to/omrigm/run-machine-learning-models-in-your-browser-with-tensorflow-js-reactjs-48pe).

Ideally, this model should connect to an indexer data in real time and feed the data to an algorithm that would estimate the probability of an event such as default and predict the future price of the asset. 

In case the model is served using Flask the API should securely connect the model and the output of the model to prevent bad actors from cheating.

Another potential obstacle is serving smart contracts on the fly. A viable solution to connecting counter parties would be standardizing the contracts and educating the users about its potential risks. Auditing these contracts is also a significant concern.

## Further Resources

[Developer Office Hours | Algorand Indexer](https://www.youtube.com/watch?v=m8gooZ_VDeY)

[Smart Contracts: Modes of Use](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/smartsigs/modes/)

[Algorand Testnet](https://developer.algorand.org/docs/get-details/algorand-networks/testnet/)

[Testnet Faucet](https://bank.testnet.algorand.network/)

[Examples using AlgoSigner:  Web App](https://purestake.github.io/algosigner-dapp-example/)

[Tutorial: Adding Transaction Capabilities to a dApp Using AlgoSigner](https://developer.algorand.org/tutorials/adding-transaction-capabilities-dapp-using-algosigner/)

[Purestake Code samples](https://developer.purestake.io/code-samples)

[Algorand Partner Training | Overview of Stateful and Stateless Smart Contracts](https://www.youtube.com/watch?v=9EpGKexKeMk)

[Using VUE.JS and Reach](https://developer.algorand.org/tutorials/using-vuejs-and-reach/)
