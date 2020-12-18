import { Component, OnInit } from '@angular/core';
import { IndexService as WeatherService } from '../../../services/weather/index.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  // template: `
  //   <app-form (parentFun)="parentFun($event)"></app-form>
  //   <app-result *ngIf="result" [weather]="result"></app-result>
  // `,
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {
  result: any = null;

  constructor(
    private weatherService: WeatherService,
  ) {
  }

  ngOnInit(): void {
  }
  parentFun(formData) {
    // console.log(formData);
    // this.result = Object.assign({}, formData, {cache: true});

    this.weatherService.query(formData.name)
      .subscribe(data => {
        console.log(data)
        this.result = data;
      })
  }
}
