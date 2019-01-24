<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Passengers</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.person-modal>Add Person</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Class</th>
              <th scope="col">Survived?</th>
              <th scope="col">Sex</th>
              <th scope="col">Age</th>
              <th scope="col"># Sib/Spouse</th>
              <th scope="col">#Parent Children</th>
              <th scope="col">Fare</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(person, index) in people" :key="index">
              <td>{{ person.name}}</td>
              <td>{{ person.passengerClass}}</td>
              <td>
                <span v-if="person.survived">Yes</span>
                <span v-else>No</span>
              </td>
              <td>{{ person.sex}}</td>
              <td>{{ person.age}}</td>
              <td>{{ person.siblingsOrSpousesAboard}}</td>
              <td>{{ person.parentsOrChildrenAboard }}</td>
              <td>{{ person.fare}}</td>
              <td>
                <button
                        type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.person-update-modal
                        @click="editPerson(person)">
                    Update
                </button>
                <br>
                <br>
                <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeletePerson(person)">
                    Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addPersonModal"
             id="person-modal"
             title="Add a new person"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">

    
      <b-form-group id="form-name-group"
                    label="Name"
                    label-for="form-name-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addPersonForm.name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
  

        <b-form-group id="form-class-group"
                      label="Passenger Class:"
                      label-for="form-class-input">
            <b-form-input id="form-class-input"
                          type="text"
                          v-model="addPersonForm.class"
                          required
                          placeholder="Enter Passenger Class">
            </b-form-input>
          </b-form-group>

        <b-form-group id="form-survived-group">
          <b-form-checkbox-group v-model="addPersonForm.survived" id="form-checks">
            <b-form-checkbox value="true">Survived?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

         
         <b-form-group id="form-sex-group"
                      label="Passenger Sex:"
                      label-for="form-sex-input">
            <b-form-input id="form-sex-input"
                          type="text"
                          v-model="addPersonForm.sex"
                          required
                          placeholder="Enter Passenger sex">
            </b-form-input>
          </b-form-group>

 <b-form-group id="form-age-group"
                      label="Passenger Age:"
                      label-for="form-age-input">
            <b-form-input id="form-age-input"
                          type="text"
                          v-model="addPersonForm.age"
                          required
                          placeholder="Enter Passenger age">
            </b-form-input>
          </b-form-group>


    
 <b-form-group id="form-siblingsOrSpousesAboard-group"
                      label="# Sibling or Spouses Abroad"
                      label-for="form-siblingsOrSpousesAboard-input">
            <b-form-input id="form-siblingsOrSpousesAboard-input"
                          type="text"
                          v-model="addPersonForm.siblingsOrSpousesAboard"
                          required
                          placeholder="Enter # Siblings or Spouses Abroad">
            </b-form-input>
          </b-form-group>

    
 <b-form-group id="form-parentsOrChildrenAboard-group"
                      label="# Parents Or Children Aboard"
                      label-for="form-parentsOrChildrenAboard-input">
            <b-form-input id="form-parentsOrChildrenAboard-input"
                          type="text"
                          v-model="addPersonForm.parentsOrChildrenAboard"
                          required
                          placeholder="Enter # Parents Or Children Aboard">
            </b-form-input>
          </b-form-group>


<b-form-group id="form-fare-group"
                      label="Passenger Fare:"
                      label-for="form-fare-input">
            <b-form-input id="form-fare-input"
                          type="text"
                          v-model="addPersonForm.fare"
                          required
                          placeholder="Enter Fare">
            </b-form-input>
          </b-form-group>


        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>







    <b-modal ref="editPersonModal"
             id="person-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">

      

       <b-form-group id="form-name-edit-group"
                    label="Name"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editPersonForm.name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
  

        <b-form-group id="form-class-edit-group"
                      label="Passenger Class:"
                      label-for="form-class-edit-input">
            <b-form-input id="form-class-edit-input"
                          type="text"
                          v-model="editPersonForm.class"
                          required
                          placeholder="Enter Passenger Class">
            </b-form-input>
          </b-form-group>

        <b-form-group id="form-survived-edit-group">
          <b-form-checkbox-group v-model="editPersonForm.survived" id="form-edit-checks">
            <b-form-checkbox value="true">Survived?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

         
         <b-form-group id="form-sex-edit-group"
                      label="Passenger Sex:"
                      label-for="form-sex-edit-input">
            <b-form-input id="form-sex-input"
                          type="text"
                          v-model="editPersonForm.sex"
                          required
                          placeholder="Enter Passenger sex">
            </b-form-input>
          </b-form-group>

 <b-form-group id="form-age-edit-group"
                      label="Passenger Age:"
                      label-for="form-age-edit-input">
            <b-form-input id="form-age-edit-input"
                          type="text"
                          v-model="editPersonForm.age"
                          required
                          placeholder="Enter Passenger age">
            </b-form-input>
          </b-form-group>


    
 <b-form-group id="form-siblingsOrSpousesAboard-edit-group"
                      label="# Sibling or Spouses Abroad"
                      label-for="form-siblingsOrSpousesAboard-edit-input">
            <b-form-input id="form-siblingsOrSpousesAboard-edit-input"
                          type="text"
                          v-model="editPersonForm.siblingsOrSpousesAboard"
                          required
                          placeholder="Enter # Siblings or Spouses Abroad">
            </b-form-input>
          </b-form-group>

    
 <b-form-group id="form-parentsOrChildrenAboard-edit-group"
                      label="# Parents Or Children Aboard"
                      label-for="form-parentsOrChildrenAboard-edit-input">
            <b-form-input id="form-parentsOrChildrenAboard-edit-input"
                          type="text"
                          v-model="editPersonForm.parentsOrChildrenAboard"
                          required
                          placeholder="Enter # Parents Or Children Aboard">
            </b-form-input>
          </b-form-group>


<b-form-group id="form-fare-edit-group"
                      label="Passenger Fare:"
                      label-for="form-fare-edit-input">
            <b-form-input id="form-fare-edit-input"
                          type="text"
                          v-model="editPersonForm.fare"
                          required
                          placeholder="Enter Fare">
            </b-form-input>
          </b-form-group>

      


        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>


<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      people: [],
      addPersonForm: {
        name: '',
        class: '',
        survived: [],
        sex: '',
        age: '',
        siblingsOrSpousesAboard: '',
        parentsOrChildrenAboard: '',
        fare: '',
      },
      editPersonForm: {
        name: '',
        class: '',
        survived: [],
        name: '',
        sex: '',
        age: '',
        siblingsOrSpousesAboard: '',
        parentsOrChildrenAboard: '',
        fare: '',
      },
      message: '',
      showMessage: false,
      ROOT_API: process.env.ROOT_API,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getPeople() {
      const path = `${this.ROOT_API}/api/v1/people`;
      axios.get(path)
        .then((res) => {
          this.people = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addPerson(payload) {
      const path = `${this.ROOT_API}/api/v1/people`;
      axios.post(path, payload)
        .then(() => {
          this.getPeople();
          this.message = 'Person added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPeople();
        });
    },
    updatePerson(payload, personID) {
      const path = `${this.ROOT_API}/api/v1/people/${personID}`;
      axios.put(path, payload)
        .then(() => {
          this.getPeople();
          this.message = 'Person updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPeople();
        });
    },
    removePerson(personID) {
      const path = `${this.ROOT_API}/api/v1/people/${personID}`;
      axios.delete(path)
        .then(() => {
          this.getPeople();
          this.message = 'Person removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPeople();
        });
    },
    initForm() {
      this.addPersonForm.name = '';
      this.addPersonForm.class = '';
      this.addPersonForm.survived = [];
      this.addPersonForm.passengerClass
      this.addPersonForm.name = '';
      this.addPersonForm.sex = '';
      this.addPersonForm.age = '';
      this.addPersonForm.siblingsOrSpousesAboard = '';
      this.addPersonForm.parentsOrChildrenAboard = '';
      this.addPersonForm.fare = '';
        
      this.editPersonForm.name = '';
      this.editPersonForm.class = '';
      this.editPersonForm.survived = [];
      this.editPersonForm.passengerClass
      this.editPersonForm.name = '';
      this.editPersonForm.sex = '';
      this.editPersonForm.age = '';
      this.editPersonForm.siblingsOrSpousesAboard = '';
      this.editPersonForm.parentsOrChildrenAboard = '';
      this.editPersonForm.fare = '';


    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addPersonModal.hide();
      let survived = false;
      if (this.addPersonForm.survived[0]) survived = true;

      const payload = {
        name: this.addPersonForm.name,
        passengerClass: parseInt(this.addPersonForm.class),
        survived : survived,
        sex : this.addPersonForm.sex,
        age : parseInt(this.addPersonForm.age),
        siblingsOrSpousesAboard : parseInt(this.addPersonForm.siblingsOrSpousesAboard),
        parentsOrChildrenAboard : parseInt(this.addPersonForm.parentsOrChildrenAboard),
        fare : parseFloat(this.addPersonForm.fare)
      };
      console.log("The Payload is ", payload)
      this.addPerson(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPersonModal.hide();
      let read = false;
      let survived = false;
      if (this.editPersonForm.survived[0]) survived = true;

      const payload = {
        name: this.editPersonForm.name,
        passengerClass: parseInt(this.editPersonForm.class),
        survived : survived,
        sex : this.editPersonForm.sex,
        age : parseInt(this.editPersonForm.age),
        siblingsOrSpousesAboard : parseInt(this.editPersonForm.siblingsOrSpousesAboard),
        parentsOrChildrenAboard : parseInt(this.editPersonForm.parentsOrChildrenAboard),
        fare : parseFloat(this.editPersonForm.fare)
      };

      this.updatePerson(payload, this.editPersonForm.uuid);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addPersonModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPersonModal.hide();
      this.initForm();
      this.getPeople(); 
    },
    onDeletePerson(person) {
      this.removePerson(person.uuid);
    },
    editPerson(person) {
      this.editPersonForm = person;
    },
  },
  created() {
    this.getPeople();
  },
};
</script>
