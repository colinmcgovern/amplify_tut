import React, { useState, useEffect } from 'react';
import './App.css';
import CommentAdd from './components/AddComment'

const App = () => {
	return(
		<div>
			<h3>Comments</h3>
			<CommentAdd />
		</div>
	)
};

export default App;
