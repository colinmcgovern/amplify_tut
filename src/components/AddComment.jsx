import React, { useState } from 'react';
import PropTypes from 'prop-types';
import '../App.css';

class AddComment extends React.Component{

	constructor(props){
		super(props)
    this.state = {}    
	}

  onChange(field, value){
    this.setState({[field]: value})
  }

	render() {
		return(
			<div>
				<form onSubmit={this.handleSubmit}>	
					<table>
						<tr>
							<td>Username</td>
							<td><input type="text" name='username'  onChange={this.onChange.bind(this)}/></td>
						</tr>
						<tr>
							<td>Comment</td>
							<td><input type="text" name='comment'  onChange={this.onChange.bind(this)} /></td>
						</tr>
						<tr>
							<td><input type="submit" value="Submit"/></td>
						</tr>
					</table>
				</form>
			</div>
		)			
	}
};

export default AddComment;
