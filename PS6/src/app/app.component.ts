import { Component } from '@angular/core';
import data from '../../mock/weather.json';
// import data from '../../mock/no.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'PS6';
  weather: any = null;

  constructor () {
    console.log(data)
  }

  onSearch() {
    this.weather = data;
  }
}
