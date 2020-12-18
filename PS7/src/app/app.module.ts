import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { IndexComponent } from './components/weather/index/index.component';
import { FormComponent } from './components/weather/form/form.component';
import { ResultComponent } from './components/weather/result/result.component';

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    FormComponent,
    ResultComponent
  ],
  imports: [
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
