import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {
  searchForm;
  city_name: string;

  @Output('parentFun') parentFun: EventEmitter<any> = new EventEmitter();

  constructor(
    private formBuilder: FormBuilder,
  ) {
    // this.searchForm = this.formBuilder.group({
    this.searchForm = new FormGroup({
      name: new FormControl(this.city_name, [
        Validators.required,
        Validators.minLength(2),
      ]),
    });
  }

  get name() { return this.searchForm.get('name'); }

  ngOnInit(): void {
  }

  onSubmit(customerData) {
    if (this.searchForm.valid) {
      // console.log('form submitted');
      // this.searchForm.reset();
      // console.warn('Your order has been submitted', customerData);

      this.parentFun.emit(customerData);
    } else {
      // validate all form fields
    }
  }
}
