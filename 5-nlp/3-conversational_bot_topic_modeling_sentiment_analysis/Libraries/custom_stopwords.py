class tools:

    def my_stopwords(_tokensIn):
        """
        Cleans a list of tokens by removing specific unwanted tokens.

        This function iterates through a list of tokens and removes any that are found 
        in the predefined `_toDelete` list.

        Args:
        _tokensIn (list of str): The input list of tokens to be cleaned.

        Returns:
        list of str: A cleaned list of tokens with specific words removed.
        """
        
        _toDelete = ['tigre', 'buenos', 'aires', 'victoria', 'josé', 'dellagiovanna', 'zona', 'norte']

        _tokens = _tokensIn[:]
        for token in _tokensIn:
            if token in _toDelete:
                _tokens.remove(token)

        return _tokens