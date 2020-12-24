# bitcoinsays

[bitcoinsays.com](https://bitcoinsays.com) decodes bitcoin addresses to reveal the [hidden messages](http://www.righto.com/2014/02/ascii-bernanke-wikileaks-photographs.html) in the blockchain

We spit the location pathname and take the 1st string as the transaction ID, and if here is one, the 2nd string as the output to highlight.

We use the transaction ID to fetch the transaction using the [SoChain API](https://chain.so/api).

Once we have that, we get the output scripts. We then convert the hex to ascii to see if there is a message hidden there.

If no output index was specified, we show them all, if there is one specified we highlight the decoded strings from that output.

Hat tip to @massigerardi for the tips on how to get a publicly viewable message into the blockchain.
