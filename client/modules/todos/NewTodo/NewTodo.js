// @flow
import React from 'react';
import Relay from 'react-relay';
import Textfield from '../../../components/Textfield/Textfield';
import NewTodoMutation from './NewTodoMutation';

export default class NewTodo extends React.Component {
  props:{
    viewer: Object,
    router: Object
    };

  state:{
    errors: Array <Object>,
    address: {}
    };

  constructor(props:Object) {
    super(props);
    this.state = {
      errors: [],
      todo: {}
    };
  }

  createTodo(todo:Object) {
    this.setState({ todo });
    const newMutation = new NewTodoMutation({
      viewer: this.props.viewer, todo
    });
    const onSuccess = (response) => {
      const errors = response.createTodo.errors;
      this.setState({
        errors
      });
    };
    Relay.Store.commitUpdate(newMutation, { onSuccess });
  }

  render() {
    const { errors } = this.state;
    return (
      <div  >
        <Textfield 
                   label='New Todo'
                   action={this.createTodo.bind(this)}
                   errors={errors}
        />
      </div>
    );
  }
}